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
    return response.json()
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
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers : { 
      Accept: 'application/json'
     },
    redirect: "follow",
    referrerPolicy: "no-referrer",
  });
  return response.json();
}


export {postData,putData,getData}