function sleep_3s() {
    console.log('INVOKE');

    setTimeout(() => {
        console.log('Wake up!')
    }, 3000)
}

console.log('Start Sleeping');
sleep_3s();
console.log('End of Program');
