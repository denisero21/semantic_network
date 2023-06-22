drop table if exists nodes, questions, answer_variants, tasks, users, 
                     question_rating, task_rating, solved_questions,
                     solved_tasks;
                     
create table nodes(
    id int primary key,
    theme varchar(100) not NULL,
    theory text not null
);

create table questions(
    id int primary key,
    node_id integer REFERENCES nodes (id) on delete CASCADE,
    question text not null,
    rating int not null
);

create table answer_variants(
    id int primary key,
    question_id integer REFERENCES questions (id) on delete CASCADE,
    variant text not null,
    is_true boolean
);

create table tasks(
    id int primary key,
    node_id integer REFERENCES nodes (id) on delete CASCADE,
    task text not null,
    check_code text,
    rating int not null
);

create table users(
    id int primary key,
    username varchar(30) not null,
    email varchar(30) not null,
    password varchar(30) not null,
    current_node integer references nodes(id) on delete cascade
);

create table question_rating(
    id int primary key,
    question_id INTEGER REFERENCES questions(id) on delete cascade,
    user_id INTEGER REFERENCES users(id) on delete cascade,
    rate int not null
);

create table task_rating(
    id int primary key,
    task_id INTEGER REFERENCES tasks(id) on delete cascade,
    user_id INTEGER REFERENCES users(id) on delete cascade,
    rate int not null
);

create table solved_questions(
    id int primary key,
    task_id INTEGER REFERENCES tasks(id) on delete cascade,
    user_id INTEGER REFERENCES users(id) on delete cascade,
    answer varchar(50) not null
);

create table solved_tasks(
    id int primary key,
    task_id INTEGER REFERENCES tasks(id) on delete cascade,
    user_id INTEGER REFERENCES users(id) on delete cascade,
    answer varchar(50) not null
);


