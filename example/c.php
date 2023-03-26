<?php

function func1($x){
    $x++;
    return $x;
}

$a = $_GET["p1"];
$b = func1($a);
$c = strip_tags($b);
echo "<input name=\"return\" value=\" $c \" />";