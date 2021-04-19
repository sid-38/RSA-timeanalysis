from Crypto.PublicKey import RSA
import timeit
iterations = 50

# Analysing the time taken for generating keys for RSA
print("Analysing time taken for generating keys for RSA")
setup = '''
from Crypto.PublicKey import RSA
'''
keygen_data=[]
for keysize in range(1024,4000,512):
    key = None
    duration = timeit.timeit(setup=setup, stmt=f"key = RSA.generate({keysize})", number=iterations)/iterations
    keygen_data.append((keysize, duration))

# Analysing the time taken for encrypting data in RSA
print("Analysing the time taken for encrypting data in RSA")
encrypt_data=[]
for keysize in range(1024,4000,512):
    setup = f'''
from Crypto.PublicKey import RSA
key = RSA.generate({keysize})
'''
    duration = timeit.timeit(setup=setup, stmt=f'key.publickey().encrypt(1234,32)', number=iterations)/iterations
    encrypt_data.append((keysize, duration))

# Analysing the time taken for decrypting data in RSA
print("Analysing the time taken for decrypting data in RSA")
decrypt_data=[]
for keysize in range(1024,4000,512):
    setup = f'''
from Crypto.PublicKey import RSA
key = RSA.generate({keysize})
ciphertext = key.publickey().encrypt(1024,32)
'''
    duration = timeit.timeit(setup=setup, stmt=f'key.decrypt(ciphertext)', number=iterations)/iterations
    decrypt_data.append((keysize, duration))

# Plotting data
from matplotlib import pyplot as plt
x = [point[0] for point in keygen_data]
y = [point[1] for point in keygen_data]
plt.plot(x,y,label="Key Generation")
x = [point[0] for point in encrypt_data]
y = [point[1] for point in encrypt_data]
plt.plot(x,y,label="Encryption")
x = [point[0] for point in decrypt_data]
y = [point[1] for point in decrypt_data]
plt.plot(x,y,label="Decryption")
plt.legend()
plt.xlabel("Key Size")
plt.ylabel("Time")
plt.ylim()
plt.yscale('log')
plt.title('Combined')
plt.show()
