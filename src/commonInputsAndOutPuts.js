async function postData( data = {}) {
    const response = await fetch("/moverequest", {
      method: "POST",
      mode: "cors",
      cache: "default",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      referrerPolicy: "no-referrer",
      body: JSON.stringify(data),
    });
    let output = await response.json()
    console.log(output)
    return response
}

function putData(data = {}) {
    const response = fetch("/outputgame", {
      method: "PUT",
      mode: "cors",
      cache: "default",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      referrerPolicy: "no-referrer",
      body: JSON.stringify(data),
    });
}

async function getData(url = "") {
  const response = await fetch(url, {
    method: "GET",
    //mode: "cors",
    //cache: "no-cache",
    //credentials: "same-origin",
    //headers : { 
    //  Accept: 'application/json'
    // },
    //redirect: "follow",
    //referrerPolicy: "no-referrer",
  })
  const abc = await response.json()
  console.log(abc)
  return response
}


export {postData,putData,getData}