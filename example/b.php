<?php
class Foo{
    static function func2($x){
        echo $x;
    }
}

$b = $_GET["p1"];
$a = Foo::func2($b);
echo $a;