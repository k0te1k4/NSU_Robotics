1. `w` - команда, которая покажет пользователей, залогинившихся в данный момент в системе. Кроме этого выдаётся информация: длительность подключения, адрес с которого произошло было выполнено подключение, команде, которую выполняет пользователь.
2. `iotop` позволяет увидеть, какой процесс в данный момент потребляет дисковые ресурсы.
3. Запустить процесс с определенным приоритетом можно командой: `nice -n -20..19 <CMD>`. Изменить приоритет “на ходу” можно с помощью: `renice -20..19 <PID>`
4. Для периодического выполнения команд используется `watch`.
Ее можно применять при скачивании больших файлов - в одном терминале качать, а в другом набрать
`watch ls -h`,
чтобы отслеживать, как растет файл (и прикидывать, когда закончится закачка).
5. `lsof`.
Она позволяет увидеть, какие процессы в системе держат файлы открытыми. Это бывает полезно, когда нужно размонтировать раздел, но система не дает это сделать.
6. `ps` Вывести список процессов.
7. `scp` Копировать файлы между хостами (для этого используется ssh).
8. `rsync` Также для синхронизации директорий между хостами можно использовать rsync (-a — archive mode, позволяет скопировать полностью всё содержимое директории «как есть», -v — вывод на консоль дополнительной информации):
9. `df` показывает размер, используемое и доступное место на подключенных файловых системах компьютера.
10. `whoami` показывает под каким именем сейчас пользователь работает в системе.