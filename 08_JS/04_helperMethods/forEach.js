// ES5 for loop
// var colors = [ 'red', 'blue', 'green'];
//
// for (var i = 0; i < colors.length; i++) {
//     console.log(colors[i]);
// }

// ES6+
const colors = ['red' , 'blue', 'green'];

colors.forEach(color => {
    console.log(color)
});

function handlePosts() {
    const posts = [
        { id: 23, title: 'Daily js news' },
        { id: 34, title: 'Daily python news' },
        { id: 53, title: 'Daily ruby news' },
    ];

     posts.forEach(post => {
        savePost(post);
    })
}

handlePosts();





