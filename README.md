# FuriganaBot
It's a pretty roughshod amalgamation of a number of libraries, so it's going to be jank. LMK if you know any quick improvements. 
1. Follow [this](https://cloud.google.com/vision/docs/setup), it'll give you a key file, assign the path to the environment variable "GOOGLE_APPLICATION_CREDENTIALS" on line 8. You'll need to put in payment details for this, but you'll only be charged if you do more than a 1000 requests per month (images) - and then it's still pretty cheap. 
2. Install the necessary dependancies in terminal: 
```pip install --upgrade google-cloud-vision watchdog pyperclip```
3. Install [yomichan](https://chrome.google.com/webstore/detail/yomichan/ogmnaimimemjmbakcfefmnahgdfhfami?hl=en-US) on your browser and enable clipboard text monitoring. 
4. Run the google_ocr_main.py file in a terminal that has been run as administrator (to allow it to look at the folder where your snip application stores snips - you may need to update this location in the file based on OS, should be googlable). 
5. Shift+Win+S a location with japanese text. Vertical text and text with furigana will be harder to parse, but usually works. The yomichan window that pops up is often poorly sized, so keep it open and it will update on subsequent snips. I personally recommend using Win+RightArrow on it to put it on the right of the screen, then resizing as needed. 
