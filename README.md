# Ginkgo Test

## Instructions:

This assumes you have `python` and `redis` installed. if not, please install the latest version of [`python3`](https://www.python.org/downloads/) and [`redis`](https://redis.io/download) before continuing.

#### 1. clone the git repo:
```bash
git clone https://github.com/chanana/gnkg.git
```

#### 2. Then run:
```bash
cd gnkg; chmod +x ./setup.sh; ./setup.sh
```

#### 3. Finally, navigate to 
        http://127.0.0.1:8000/gnkg/submit


## Example
If you search for `"catttctatc"`, you might get a result in the form of `Your DNA string was found in Megavirus chiliensis, complete genome at complement(77858..79345) as a part of YP_004894136.1.` If there are other locations in other genomes where this sequence is present, they may be returned instead since the search is random each time.

## Features / Limitations:
- The length of input is limited to 1000 characters
- The input DNA sequence can be uppercase or lowercase, it gets converted to uppercase.
- If the sequence is present _at all_, it will be found. If multiple instances are present, App will return a random result each time.
- The "monitor" page auto-refreshes every 10 seconds to check for new submissions.

## Removing the App
To remove the app from your system, please run `redis-cli shutdown` and delete the git repo.