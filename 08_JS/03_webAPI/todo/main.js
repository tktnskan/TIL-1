const init = () => {
    const todoBox = document.querySelector('#todo_box');
    const reverseButton = document.querySelector('#reverse_btn');
    const fetchButton = document.querySelector('#fetch_btn');
    const input = document.querySelector('#add_todo_input');
    const addButton = document.querySelector('#add_todo_btn');

    input.addEventListener('keydown', e => {
       if (e.key === 'Enter') {
           todoBox.appendChild(createTodo(input.value, false));
       }
    });

    addButton.addEventListener('click', e => {
        todoBox.appendChild(createTodo(input.value, false));
    });

    reverseButton.addEventListener('click', e => {
        reverseTodos()
    });

    fetchButton.addEventListener('click', e => {
        fetchData('https://koreanjson.com/todos');
    });

    const fetchData = URL => {
        fetch(URL)
            .then(res => res.json())
            .then(todos => {
                for (const todo of todos) {
                    todoBox.appendChild(createTodo(todo.title, todo.completed));
                }
            })
    };

    const createTodo = (inputText, completed = false) => {
        // Card
        const todoCard = document.createElement('div');
        todoCard.classList.add('ui', 'segment', 'todo-item');
        if (completed) todoCard.classList.add('secondary');
        // Card > Wrapper
        const wrapper = document.createElement('div');
        wrapper.classList.add('ui', 'checkbox');
        // Card > Wrapper > input (checkbox)
        const input = document.createElement('input');
        input.setAttribute('type', 'checkbox');
        input.checked = completed;

        input.addEventListener('click', e => {
            if (completed) {
                label.classList.remove('completed-label');
                todoCard.classList.remove('secondary');
            } else {
                label.classList.add('completed-label');
                todoCard.classList.add('secondary');
            }
            completed = !completed;
        });
        // Card > Wrapper > label (text)
        const label = document.createElement('label');
        label.innerHTML = inputText;
        if (completed) label.classList.add('completed-label');
        // Card > Icon
        const deleteIcon = document.createElement('i'); // <i></i>
        deleteIcon.classList.add('close', 'icon', 'delete-icon');  // <i class="close icon"></i>

        deleteIcon.addEventListener('click', e => {
            todoBox.removeChild(todoCard);
        });

        wrapper.appendChild(input);
        wrapper.appendChild(label);
        todoCard.appendChild(wrapper);
        todoCard.appendChild(deleteIcon);

        return todoCard
    };

    const reverseTodos = () => {
        // Deep copy (Array.from)
        const allTodos = Array.from(document.querySelectorAll('.todo-item'));

        while (todoBox.firstChild) {
            todoBox.removeChild(todoBox.firstChild)
        }

        for (const todo of allTodos.reverse()) {
            todoBox.appendChild(todo)
        }
    };
};

init();
