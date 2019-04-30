const me = {
    name: 'Yu Tae Young',
    phone: '01012345678',
    email: 'neo@hphk.kr',
    intro: function () {
        return `Hi my name is ${this.name}.`
    }
};

console.log(me.intro());

const name = 'helloodsjsladkf;kl';

const you = {
    name: 'kim tak hee',
    phone: '01012345678',
    email: 'neo@hphk.kr',
    intro: () => {
        return `Hi my name is ${this.name}.`
    },
    wait: function () {
        setTimeout(() => {
            console.log(this.email)
        }, 1000)
    },
};

console.log(you.wait());