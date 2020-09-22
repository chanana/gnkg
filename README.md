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


## Features / Limitations:
- The length of input is limited to 1000 characters
- The input DNA sequence can be uppercase or lowercase, it gets converted to uppercase 
- If the sequence is present _at all_, it will be found. If multiple instances are present, App will return a random result each time.

## Removing the App
To remove the app from your system, please run 
`redis-cli shutdown` and delete the git repo.