const getUser = id => {
    const users = [
        { id: 1, githubID: 'eduyu' },
        { id: 2, githubID: 'edujohn' },
    ];

    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            const user = users.find(user => user.id === id);
            if (user) resolve(user);
            else reject(new Error(`Can't find user ${id}`));
        }, 2000)
    });
};

const getRepos = user => {
    const repos = ['TIL', 'Workshop_HW', 'Python', 'JS'];

    return new Promise((resolve, reject) => {
        setTimeout(()=>{
            if (repos) resolve(repos);
            else reject(new Error('No REPOs'))
        }, 1000);
    });
};

const getCommits = repo =>  {
    const commits = ['Init repo', 'Make index.html'];

    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            if (commits) {
                resolve(commits);
            } else {
                reject(new Error('ERRRRRRORRR'));
            }
        }, 2000)
    });
};

getUser(1)
    .then(user => getRepos(user))
    .then(repos => getCommits(repos[0]))
    .then(commits => console.log(commits.length))
    .catch(err => console.error(err));

// user = getUser(1);
// // repos = getRepos(user);
// // commits = getCommits(repos[0])
// // time = getTimeFromCommit(commits[0])



