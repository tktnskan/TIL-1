function complexTask() {
    for (let i = 0; i < 1000000000; i++) {}
    console.log('오-래 걸림');
}

setTimeout(() => console.log('1ms 걸림'), 1);
complexTask();