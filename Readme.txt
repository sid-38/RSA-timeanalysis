* Create a virtual environment using the command 'python3 -m venv venv'
* Activate the virtual environment using "source venv/bin/activate"
* Install the requirements using "pip install -r requirements.txt"
* Run the program using "python3 RSA.py"

If the following error occurs:
	AttributeError: module 'time' has no attribute 'clock'
* Open the file ./venv/lib/python3.8/site-packages/Crypto/Random/_UserFriendlyRNG.py
* Change the occurence of "time.clock()" to "time.time()". This would probably be in line 77 in the file. 

The reason for the error is that pycrypto is no longer actively maintained and hence has not been updated after python3.8 dropped support for the function time.clock(). Downgrading python3.8 to python3.7 should also work instead of changing as shown above. 
