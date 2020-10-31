create table category(
    codename varchar(255) primary key,
    name varchar(255),
    aliases text
);

create table expense(
    id integer primary key,
    amount integer,
    created datetime,
    category_codename integer,
    raw_text text,
    FOREIGN KEY(category_codename) REFERENCES category(codename)
);

insert into category(codename, name, aliases)
values
    ('products', '🍟 Продукты', 'еда, продукты'),
    ('dinner', '🍽 Обед', 'столовая, ланч, обед'),
    ('transport', '🚌 Проезд', 'автобус, трамвай, такси, проезд'),
    ('internet', '🌐 Интернет', 'инет, интернет'),
    ('bank', '🏦 Банк', 'сбер, банк, крата'),
    ('telephone', '📱 Телефон', 'телефон, мтс, связь'),
    ('other', '🗑 Прочее', 'прочее, ерунда');

