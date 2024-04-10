# Text-Hider

# PROJECT TITLE/PROBLEM STATEMENT
The former consists of linguistic or language forms of hidden writing. The later, such as invisible ink, try of hide messages physically. One disadvantage of linguistic steganography is that users must equip themselves to have a good knowledge of linguistry. In recent years, everything is trending toward digitization. And with the development of the internet technology, digital media can be transmitted conveniently over the network. Therefore, messages can be secretly carried by digital media by using the steganography techniques, and then be transmitted through the internet rapidly Steganography is the art of hiding the fact that communication is taking place, by hiding information in other information. Many different carrier file formats can be used, but digital images are the most popular because of their frequency on the internet. For hiding secret information in images, there exists a large variety of steganography techniques some are more complex than others and all of them have respective strong and weak points. So we prepare this application, to make the information hiding more simple and user friendly.

# AGENDA
1. The goal of steganography is covert communication. So, a fundamental requirement of this steganography system is that the hider message carried by stego-media should not be sensible to human beings. 
2. The other goad of steganography is to avoid drawing suspicion to the existence of a hidden message. This approach of information hiding technique has recently became important in a number of application area
3.This project has following objectives:
-> To product security tool based on steganography techniques. 
-> To explore techniques of hiding data using encryption module of this project 
-> To extract techniques of getting secret data using decryption module.

# PROJECT  OVERVIEW
1. The main goal of this projects it to communicate securely in a completely undetectable manner and to avoid drawing suspicion to the transmission of a hider data. There has been a rapid growth of interest in steganography for two reasons: 
-> The publishing and broadcasting industries have become interested in techniques for hiding encrypted copyright marks and serial numbers in digital films, audio recordings, books and multimedia products Moves by various governments to restrict the availability of encryption services have motivated people to study methods by which private messages can be embedded in seemingly innocuous cover messages. 
-> The basic model of steganography consists of Carrier, Message and password. Carrier is also known as cover-object, which the message is embedded and serves to hide the presence of the message.
2. Basically, the model for steganography is shown on following figure
![image](https://github.com/AmanJoshi1604/Text-Hider/assets/125122061/6f73207a-9036-4c85-b57f-05a2fc8e731f)
3. Message is the data that the sender wishes to remain it confidential. It can be plain text, ciphertext, other image, or anything that can be embedded in a bit stream such as a copyright mark, a covert communication, or a serial number. Password is known as stego-key, which ensures that only recipient who know the corresponding decoding key will be able to extract the message from a cover-object. The cover-object with the secretly embedded message is then called the Stego-object. Recovering message from a stego-object requires the cover-object itselt and a corresponding decoding key if a stego-key was used during the encoding process. The original image may or may not be required in most applications to extract the message. 
4. Recovering message from a stego-object requires the cover-object itselt and a corresponding decoding key if a stego-key was used during the encoding process. The original image may or may not be required in most applications to extract the message. 
5. There are several suitable carriers below to be the cover-object: 
-> Network protocols such as TCP, IP and UDP 
-> Audio that using digital audio formats such as wav, midi, avi, mpeg, mpi and voc 
-> File and Disk that can hides and append files by using the slack spac
-> Text such as null characters, just alike morse code including html and java 
-> Images file such as bmp, gif and jpg, where they can be both color and gray-scale.
6. In general, the information hiding process extracts redundant bits from cover-object. The process consists of two steps:
-> Identification of redundant bits in a cover-object. Redundant bits are those bits that can be modified without corrupting the quality or destroying the integrity of the cover-object. 
-> Embedding process then selects the subset of the redundant bits to be replaced with data from a secret message. The stego-object is created by replacing the selected redundant bits with message bits

# WHO ARE THE END USERS of this project ?
1. Corporate Security : Companies might employ steganography to protect proprietary information, trade secrets, or sensitive corporate communications.
2. Digital Rights Management (DRM) : Steganography can be employed for digital rights management, where copyright protection and information about authorized users are embedded within digital media files.
3. Cybersecurity Professionals : Security experts may use steganography as a tool for testing the security of systems and networks, uncovering potential vulnerabilities.
4. Researchers and Academia : Researchers may use steganography in various fields, including computer science and cryptography, to explore new methods or analyze the strengths and weaknesses of existing techniques.
5. Everyday Users : In some cases, individuals may use steganography for personal reasons, such as hiding messages within images for fun, artistic expression, or as a way of preserving privacy in personal communications.
6. Journalists and Whistleblowers : Individuals working in fields that require discretion, such as journalists and whistleblowers, might use steganography to hide information and protect their sources.

# SOLUTION AND ITS VALUE PROPOSITION
Present inside data_hider.py file.

# How did you customize the project and make it your own
![image](https://github.com/AmanJoshi1604/Text-Hider/assets/125122061/bcb16ac3-921a-490d-b2d8-42e15b75ed03) ----------> ![image](https://github.com/AmanJoshi1604/Text-Hider/assets/125122061/0398b0c7-0067-44f8-bc4b-c781d24405a4)

In the above image you can see that firstly I had uploaded the picture in the picture box and added some text to the text box and I can hide this text inside the image using my project. After that it will create an encrypted image in which the text is hiding and it cannot be decrypted until and unless the image is decrypted with this program. That will the validation of my project key. 

# Modelling
![image](https://github.com/AmanJoshi1604/Text-Hider/assets/125122061/f19baf5e-dd91-4d9a-80da-39a4bc67082d)

# Result
------> ![image](https://github.com/AmanJoshi1604/Text-Hider/assets/125122061/4295b61b-4616-48d3-9aa4-f7f21045aaff)                 
------> ![image](https://github.com/AmanJoshi1604/Text-Hider/assets/125122061/231e9a17-13fa-45ce-8c05-1d051297b1a5)               
------> ![image](https://github.com/AmanJoshi1604/Text-Hider/assets/125122061/c3bbcec3-d0dc-4700-a23e-6f846da97bdd)              
------> ![image](https://github.com/AmanJoshi1604/Text-Hider/assets/125122061/1cbb0fa5-81f0-4fc6-bfcf-d042039cccdd)           
------> ![image](https://github.com/AmanJoshi1604/Text-Hider/assets/125122061/8529b9aa-c72a-489f-a90f-5f94003d29f0)                
------> ![image](https://github.com/AmanJoshi1604/Text-Hider/assets/125122061/2093505b-8394-4374-9b6a-4b195c556894)          
