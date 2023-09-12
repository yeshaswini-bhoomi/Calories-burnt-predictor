// document.getElementById('submit').addEventListener('click', func);

async function func(e) {
    // e.preventDefault()
    console.log(document.getElementById('gender').value);
    let gender = document.getElementById('gender').value == 'male' ? 0 : 1;
    let age = document.getElementById('age').value;
    let height = document.getElementById('height').value;
    let weight = document.getElementById('weight').value;
    let duration = document.getElementById('duration').value;
    let heartrate = document.getElementById('heartrate').value;
    let bodytemp = document.getElementById('bodytemp').value;
   
    console.log("sending to backend: "+gender+" ,"+age+" ,"+height+" ,"+weight+" ,"+duration+" ,"+heartrate+" ,"+bodytemp);
   
    const data1 = await fetch("http://127.0.0.1:5000/", {
        method: "POST",
        body: JSON.stringify({
            gender, age, height, weight, duration, heartrate, bodytemp
        }),
        headers: {
            "Content-type": "application/json"
        }
    }).then(res=>res=res.json()).then(data=>{
        console.log(data);
        
        document.getElementById('output').innerText=`You have burnt ${data.result} calories`;
    });
    
    


}