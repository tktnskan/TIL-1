// fetch.js ES6+ BROWSER
const DOMAIN = 'https://jsonplaceholder.typicode.com/';
const RESOURCE = 'posts';
const QUERY_STRING = '';

const URL = DOMAIN + RESOURCE + QUERY_STRING;

// (만들고) => 정보를 담고 => 보내고 => 기다리고 => 처리한다.

const getRequest = URL => {
    fetch(URL) // 만들고 => 정보를 담고 => 보내고
        .then(response => response.json()) // 기다리고 => 도착한 데이터를 파싱함.
        .then(parseData => console.log(parseData)); // 파싱한 데이터를 출력한다.
};

const postRequest = URL => {
    fetch(URL, {
        method: 'POST',
        body: JSON.stringify({
            value: 10
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
    })
        .then(response => response.json()) // 기다리고 => 도착한 데이터를 파싱함.
        .then(parseData => document.appendChild('<h1>')); // 파싱한 데이터를 출력한다.
};



