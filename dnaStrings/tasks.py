import fnmatch
import json
import os
import random
import re

from Bio import SeqIO
from Bio.Seq import Seq

from dnaStrings.models import Tasks
from gnkg.celery import app
from gnkg.settings import BASE_DIR


@app.task(bind=True)
def findProtein(self, job_name=None, dna_string=None):
    model_instance = Tasks(
        task_id=self.request.id, job_name=job_name, dna_string=dna_string, dna_result="pending",
    )
    print(job_name, dna_string)
    # b.save()

    # Declare variables
    path = os.path.join(BASE_DIR, "dnaStrings/static/dnaStrings")
    # make a list of file paths
    files = [entry.path for entry in os.scandir(path) if fnmatch.fnmatch(entry.name, r"[NC]*.txt")]
    random.shuffle(files)  # shuffle the file list before searching to simulate randomness
    dna = Seq(dna_string.upper())  # make sure to correct for upper case

    with open(os.path.join(path, "term_to_description_dict.json"), "r") as input_handle:
        nc_to_description = json.load(input_handle)

    result = get_results(files, dna)
    if result:
        loc, prot, nc = get_useful_stuff_from_result(result)
        model_instance.dna_result = (
            f"Your DNA string was found in {nc_to_description[nc]} at {loc} as a part of {prot}."
        )
        model_instance.save()
    else:
        model_instance.dna_result = "Not Found!"
        model_instance.save()


def get_useful_stuff_from_result(result):
    description = result.description  # get the description as a string

    # explanation of regex: find either "location=[number..number]"
    # or "location=complement(number..number)"
    regex = re.compile(r"location=(complement\()?\d+..\d+(\))?")

    loc = regex.search(description)  # this is a Match object
    # convoluted way of removing "location=" and the final "]"
    final_location = description[loc.start() : loc.end()].split("location=")[1]

    # do similar thing for protein id
    regex = re.compile(r"protein_id=.*]")
    prot = regex.search(description)  # this is a Match object
    # convoluted way of removing "protein_id=" and the final "]"
    final_protein = (
        description[prot.start() : prot.end()].split("protein_id=")[1].split(" ")[0][:-1]
    )

    # get NC number
    regex = re.compile(r"NC_[0-9]+")
    nc_number = regex.search(result.id).group(0)

    return (final_location, final_protein, nc_number)


# go through the list of files, as soon as you get a hit, return that hit.
# since the file list itself is randomized, ideally you'd get different results each time
# unless there is only one instance of the string in all the files.
def get_results(file_list, dna):
    #     results = []
    for filename in file_list:
        # print(filename)
        with open(filename, "r") as input_handle:
            for record in SeqIO.parse(input_handle, "fasta"):
                if "complement" in record.description:
                    result = re.findall(str(dna.reverse_complement()), str(record.seq))
                else:
                    result = re.findall(str(dna), str(record.seq))
                if result:
                    # print(record)
                    return record
