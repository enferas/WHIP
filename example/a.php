<?php

function func1($a){
    $a++;
    return $a;
}
$a = $_GET["p1"];
$a = func1($a);
echo $a;