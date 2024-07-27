def ignore_command (command): lambda: ('True' if word in command else 'False' for word in ['alias','configuration', 'ip', 'sql', 'select', 'update', 'exec','del', 'truncate'])
