'''
Steps for LSB stego
    1) Grab image details
    2) Read payload and encrypt it
    3) Determine if image is large enough to hold payload
    4) Convert payload data to binary
    5) iterate over image and store information in least significant bits of each pixel 
    6) save the new image
'''
class Stego:


