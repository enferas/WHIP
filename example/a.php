<?php

function func1($a){
    $a++;
    return $a;
}
$a = $_GET["p1"];
$b = func1($a);
echo $b;