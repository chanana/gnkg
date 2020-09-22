# Ginkgo Test

## Instructions:

#### 1. clone the git repo:
```bash
git clone https://github.com/chanana/gnkg.git
```

#### 2. `cd` into folder and run:
```bash
cd gnkg
./setup.sh
```

#### 3. navigate to 
        http://127.0.0.1:8000/gnkg/submit


### Features / Limitations:
- The length of input is limited to 1000 characters
- The input DNA sequence can be uppercase or lowercase, it gets converted to uppercase 
- If the sequence is present _at all_, it will be found. If multiple instances are present, App will return a random result each time.