Disclaimer:<br>
Im using raspberry pi 4 model B with 

This Code will show you how to send images from your raspberry pi to firebase :
1. Set your firebase at https://firebase.google.com/ 
![image](https://user-images.githubusercontent.com/80795963/180496938-493af277-710f-425c-b63c-6333c1d00534.png)
![image](https://user-images.githubusercontent.com/80795963/180499548-c4669f83-0b4b-42fc-8ec9-4dcbbcb2dd48.png)
![image](https://user-images.githubusercontent.com/80795963/180497230-d9d5a0d0-efa1-44db-b3af-a8f142e9391c.png)
![image](https://user-images.githubusercontent.com/80795963/180499815-f9914587-0f8f-4571-a27d-ac535eea3967.png)
![image](https://user-images.githubusercontent.com/80795963/180497795-ae76d7da-7818-4005-b550-35a6061539b6.png)
![image](https://user-images.githubusercontent.com/80795963/180498207-60b921ca-f7bf-49b1-963a-ef5c97f76e2d.png)
![image](https://user-images.githubusercontent.com/80795963/180498587-a7e3e994-d4c0-46d3-8562-40a42978ddfd.png)
![image](https://user-images.githubusercontent.com/80795963/180498872-9003bae5-a619-40c0-8d39-27ef68d1e7bb.png)
![image](https://user-images.githubusercontent.com/80795963/180591927-cff4b742-76c0-4b24-a174-a75ddcc2d036.png)<br>
rules_version = '2';<br>
service firebase.storage {<br>
  match /b/{bucket}/o {<br>
    match /{allPaths=**} {<br>
      allow read, write;<br>
    }<br>
  }<br>
}<br>
![image](https://user-images.githubusercontent.com/80795963/180591973-ad785604-457c-4d92-875a-6180d0101c80.png)
![image](https://user-images.githubusercontent.com/80795963/180592031-aeaee88c-ba2d-461a-be3f-1b33efb6061b.png)
![image](https://user-images.githubusercontent.com/80795963/180592089-b5ed18aa-db4b-4331-af40-5726f9dfce22.png)
![image](https://user-images.githubusercontent.com/80795963/180592129-77ea07df-71aa-4722-a911-537ead6b8ce3.png)
![image](https://user-images.githubusercontent.com/80795963/180592184-066d6298-10e5-4f29-a787-4f57e3c3b291.png)
![image](https://user-images.githubusercontent.com/80795963/180592241-02ba23d2-908f-4499-a442-4ea377f1fba6.png)
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAMniwDKsFBnUk9E1d3Ac3BAUsCIN35lFc",
  authDomain: "faqsendimages.firebaseapp.com",
  databaseURL: "https://faqsendimages-default-rtdb.firebaseio.com",
  projectId: "faqsendimages",
  storageBucket: "faqsendimages.appspot.com",
  messagingSenderId: "756140925503",
  appId: "1:756140925503:web:2b676767423c9f912c4e8a",
  measurementId: "G-BJYR2GCEZ3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

2. 

Fire Base : https://firebase.google.com/

reference:<br>
https://www.youtube.com/watch?v=om545WbUh2I&t=3s
