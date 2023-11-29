<?php
namespace MyNamespace;

trait Bonus {
    public function calculateBonus() {
        return $this->salary * 0.4;
    }
}

abstract class Employee {
    protected $name;
    protected $salary;

    public function __construct($name, $salary) {
        $this->name = $name;
        $this->salary = $salary;
    }

    abstract protected function calculateSalary();
}

class FullTimeEmployee extends Employee {
    use Bonus;

    public function __construct($name, $salary) {
        parent::__construct($name, $salary);
    }

    protected function calculateSalary() {
        return $this->salary + $this->calculateBonus();
    }

    public function __toString() {
        return "Nama: {$this->name}, Gaji: {$this->calculateSalary()}";
    }
}

$employee = new FullTimeEmployee("Budi", 10000000);
echo $employee;
?>
