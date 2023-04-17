async function postData( data = {}) { //posting data and expecting a response based on the data given
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
    return output
}

function putData(data = {}) { //putting data and expecting a message recieved respone
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

async function getData(url = "") {  //requesting data from a url
  const response = await fetch(url, {
    method: "GET",
  })
  const abc = await response.json()
  return abc
}


export {postData,putData,getData}