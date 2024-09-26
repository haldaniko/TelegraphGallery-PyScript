# Script for creating galleries on telegra.ph

Overview
This Python script automates the process of creating image galleries on Telegra.ph, including account creation and
uploading images to a gallery page.

## Installation

```
git clone `https://github.com/haldaniko/TelegraphGallery-PyScript.git`
cd TelegraphGallery-PyScript

# on macOS
python3 -m venv venv
source venv/bin/activate

# on Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

## Usage 

#### Step 1: Create an Account
``` bash
python create_account.py
```
- Enter the short name, author name, and author URL when prompted.
- Save the generated token and account information for further use.
#### Step 2: Create an Account
``` bash
python create_post.py
```
- Enter your Telegra.ph token, folder path for the images, and page title when prompted.
- The script will create a page and upload all images from the specified folder.


## Demo
![demo.png](screenshots%2Fdemo.png)
---
![demo2.png](screenshots%2Fdemo2.png)