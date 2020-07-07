#GIT

Git - система контроля версий для кода. Гит - это когда речь идет о коде.

Git - технология
Github, gitlab etc - хостинги, некий сервер, на котором будет лежать наш код.

Проверка того , установлен ли он - просто набрать в консоли-терминале - git.

Создадим новый репозиторий на гите.

Как мы можем локально использовать наш репозиторий?
1. Склонировать репозиторий.
в локальной какой то папку просто делаем:
git clone https://github.com/C0nstanta/15Lesson_git.git
2. Создать самостоятельно (локально) какую то дирректорию. 
инициализировать ее с помощью команды:

git init 
-
загрузить в нее какие то файлы и добавить на гитхаб

venv никогда не должен попадать на удаленный сервер.
Мы должны как то игнорировать эту папку. Как?

Изначально инициализируем нашу дирректорию с помощью :

git init
-


Можно посмотреть что у нас находится в дирректории, включая скрытые файлы

ls -la
-
(venv) (base) MacBook-Pro-admin:15Lesson admin$ ls -la
total 24
drwxr-xr-x   8 admin  staff   256 Jul  6 19:09 .
drwxr-xr-x  19 admin  staff   608 Jul  5 12:42 ..
drwxr-xr-x  14 admin  staff   448 Jul  6 19:06 .git
-rw-r--r--   1 admin  staff    19 Jul  5 23:30 .gitignore
drwxr-xr-x   6 admin  staff   192 Jul  5 12:45 .idea
-rw-r--r--   1 admin  staff  1623 Jul  6 19:09 git_manual.md
-rw-r--r--   1 admin  staff    52 Jul  5 23:30 main.py
drwxr-xr-x   6 admin  staff   192 Jul  5 12:42 venv

Далее создаем файл .gitignore
добавляем туда
venv/
.idea/
*.pyc

При запуске нашего кода пайтон запускает сначала байткод. Файлы с расширением .pyc

git status - показывает текущее состояние гит репозитория.
- 

git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        git_manual.md

git_manual.md - неотслеживаемый файл.
Что такое - отслеживание?

У нас есть проект, файлы.
Файлы могут быть :
отслеживаемыми
закомиченными
Commit - это снимок, состояние проекта.
при совершении commit, мы запсиываем состояние проекта. Что бы в будущем что то с ним сделать.
Но коммит мы можем сделать только с теми фалами, которые у нас проиндексированы(отслеживаются)

---------------------------------
Файлы , которые отслеживаются, находятся в такой штуке как :

stage
-
Перед тем как попасть в коммит , файлы находятся в stage.
И для того, что бы файлы в stage  добавить у нас существует:

git add
-

(venv) (base) MacBook-Pro-admin:15Lesson admin$ git add .
(venv) (base) MacBook-Pro-admin:15Lesson admin$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   git_manual.md

Все , что находится в stage  подлежит коммиту.

git commit -m "some text"
-
где -m - означает message
коммит нужен что бы максимально кратко сказать, что было сделано в данном изменении.


(venv) (base) MacBook-Pro-admin:15Lesson admin$ git commit -m 'ititial commit'
[master b7bad60] ititial commit
 1 file changed, 76 insertions(+)
 create mode 100644 git_manual.md


b7bad60 - хеш коммита.

- после того, как сделан комит, надо запушить на репозиторий.

- Нам нужно указать ссылку на удаленный репозиторий, куда будут загружаться все изменнения:

git remote add origin https://github.com/C0nstanta/15Lesson_git.git
-

- если remote был уже, поменять можно вот так:

git remote set-url origin https://github.com/C0nstanta/15Lesson_git.git
-

Что бы посмотреть origin:

git remote -v
-
 
Кроме того, что у нас есть репозиторий, у нас есть еще и ветки.
Ветки - такие абстракции, которые разделяют наш проект.(ответвления проекта)
основная ветка - master

Мы должны указать куда мы будем запушивать наши изменения. Имя ветки.
для этого мы прописываем:

git push -u origin master ( где -u - set-upstream) куда и будут пушиться изменения
-
origin - это указатель на то, что это у нас удаленный репозиторий.
master - имя ветки на удаленном репозитории.
---------------------------------

Совершился пуш, все ушло на удаленную ветку.
-

git log - показывает локальную историю текущей ветки.
-

Например мы пишем какой то код и в какой то момент понимаем, что то что мы пишем -оно не правильно и
хотим отменить все изменения, которые были применены после предыдущего коммита.

в таком случае мы применяем:

git checkout main.py (имя файла, в котором мы хотим отменить изменения)
-
git checkout main.py
-

git checkout . (убрать полностью все изменения)
-
Updated 1 path from the index
все изменения до коммита убрали
---------------------------------------
после того, как файл добавлен в stage, мы с помощью команды git checkout откатить его уже не 
можем.
Но с помощью reset можем


git reset - удаляет файлы из stage
-
git reset . (или имя файла)
- 
но при этом изменения, которые мы делали, все остаются, просто из stage выводим.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   main.py

если мы хотим не просто достать из stage но и еще очистить изменения мы пишем:

git reset (file) --hard
-

git reset HEAD^1  - откатывает последний локальный коммит, не отменяя изменений.
-
И это так же отменит индекс. ^1 - это значит, что откатить надо последний коммит.
^2 - последних 2 коммита.

git reset --hard HEAD^1  - откатит последний коммит и отменит все изменения.
-

Ветки - это мощные абстракции, которые решают много вопросов.
-
Каким образом используются ветки?
Обычно используется какая то ветка, в которой находится самая свежая рабочая версия программы.

в продакшене обычно существует 3(4) основных ветки:
- master
В master находится самый актуальный код, который находится в общем пользовании.

- stage
В stage находится тот код, который должен попасть на ветку  master.
Тот код, который должен быть протестирован. 
- dev (develop)
Тут ведутся все разработки.
- Все остальные ветки, которые сливаются в ветку dev. 

Нас интересует процесс слива. Как одна ветка попадает в другую.
-
За это ответствена команда :

git merge (служит для того, что бы сливать какие то изменения).
-

Допустим мы решили создать еще одну ветку и назвать ее feaches

Для того, что бы посмотреть, в какой ветке мы сейчас находимся:

git branch
-
git branch
* master

(*) Показывает где мы находимся. То есть есть одна ветка - мастер, и мы в не же и находимся.

 Создание ветки:

git branch develop
-
(venv) admin@MacBook-Pro-admin.local:~/PycharmProjects/15Lesson$git branch
  develop
* master

Для того, что бы перейти в другую ветку:

git checkout develop
-

(venv) admin@MacBook-Pro-admin.local:~/PycharmProjects/15Lesson$git checkout develop
M       git_manual.md
Switched to branch 'develop'


Если несколько людей работают с одним и тем же кодом, как понять кому - какой код трогать?
-

Обычно это понятно в процессе разделения задачи, но бывает что кто то чей то код зацепил.
Этот нюанс станет ясен тогда - когда кто то попытается эти ветки слить воедино.

Для того , что бы слить все воедино, я должен находиться в целевой ветке, в той - куда я 
хочу поместить код.
А во вторых делаю так:

git merge develop (имя ветки, из которой я хочу перенести изменения)
---

(venv) admin@MacBook-Pro-admin.local:~/PycharmProjects/15Lesson$git merge develop 
Auto-merging main.py
CONFLICT (content): Merge conflict in main.py
Automatic merge failed; fix conflicts and then commit the result.

Конфликт произошел, так как один и тот же код цеплялся в разных ветках.
Мы в main.py можем видеть что у нас где менялось.
<<<<<<< HEAD
=======
def new_function(s: str):
    if len(s) >= 100 :
        print("Hello one")
    else:
        print("Hello two")


>>>>>>> develop
if __name__ == "__main__":
    rand_def(10)
    print("Hello world!")


Если мы решили оставить все так - как есть, тогда:

git merge --abort
-

А если мы решаем конфликт, то мы в ручном режиме все правим в файле.
После того , как поправили все руками, мы пишем:

git add main.py
-

git pull - команда. которая вытаскивает изменения из удаленного репозитория.
-

по сути она делится на 2 команды:

git fetch и git merge
-

git fetch - вытаскивает изменения
-
git merge - мерджит эти изменения в ветку.
-
git rebase - перебазирование(похожа на merge, но не используется, потому что не сохраняет историю коммитов)
-

Если конфликт между локальным и удаленным репозиотрием - тогда нужно с локадьным что то решать.
Следует все наши локальне коммиты застешить.

git stash
-

Если мы хотим что то откатить с мастера, мы делаем:

git revert (и там согласно настроек)
- 

usage: git revert [<options>] <commit-ish>...
   or: git revert <subcommand>

    --quit                end revert or cherry-pick sequence
    --continue            resume revert or cherry-pick sequence
    --abort               cancel revert or cherry-pick sequence
    --skip                skip current commit and continue
    --cleanup <mode>      how to strip spaces and #comments from message
    -n, --no-commit       don't automatically commit
    -e, --edit            edit the commit message
    -s, --signoff         add Signed-off-by:
    -m, --mainline <parent-number>
                          select mainline parent
    --rerere-autoupdate   update the index with reused conflict resolution if possible
    --strategy <strategy>
                          merge strategy
    -X, --strategy-option <option>
                          option for merge strategy
    -S, --gpg-sign[=<key-id>]
                          GPG sign commit


если хотим 2 коммита назад откатить, то делаем так:

git revert master^2
-



Ключевое слово HEAD - это указатель на текущий коммит.


