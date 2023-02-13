<?php

function func1($x){
    $x++;
    return $x;
}

class Foo{
    static function func2($x){
        echo $x;
    }
}


$a = $_GET["p1"];
$b = func1($a);
$c = Foo::func2($b);
echo $c;