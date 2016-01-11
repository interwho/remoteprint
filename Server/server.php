<?php
echo file_get_contents('queue.txt');
file_put_contents('queue.txt', '');
?>