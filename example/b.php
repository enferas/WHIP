<?php

$b = $_GET["p1"];
$a = strip_tags($b);
echo "<input name=\"return\" value=\" $a \" />";