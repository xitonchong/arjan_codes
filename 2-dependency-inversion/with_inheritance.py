from abc import ABC, abstractmethod
from typing import Optional
from dataclasses import dataclass

@dataclass
class Employee(ABC):
    ''' basic representation of an employee at the company'''

    name: str
    id: int
    
    @abstractmethod
    def compute_pay(self) -> float:
        ''' compute the payout for employee'''



@dataclass
class HourlyEmployee(Employee):
    ''' employee that's paid based on the number of worked hours'''

    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost



@dataclass
class SalariedEmployee(Employee):
    ''' employe that's paid based on a fixed monthly salary'''
    
    monthly_salary: float
    percentage: float = 1
    
    def compute_pay(self):
        return self.montly_salary * self.percentage




@dataclass
class Freelancer(Employee):
    ''' freelancer that's aid based on number of worked hours.'''
    
    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self):
        return self.pay_rate * self.hours_worked



@dataclass
class HourlyEmployeeWithCommision(HourlyEmployee):
    ''' commission on top of hourly employee'''

    commission: float = 100
    contracts_landed: int = 0

    def compute_pay(self):
        return super().compute_pay() + self.commision  * self.contracts_landed


@dataclass
class FreelancerWithCommission(Freelancer):
    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed

@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):
    """Employee that's paid based on a fixed monthly salary and that gets a commission."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed



def main() -> None:
    ''' main function '''

    henry = HourlyEmployee(name="Henry", id=12321, pay_rate=50, hours_worked=100)
    print(
        f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah = SalariedEmployeeWithCommission(
        name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
    )
    print(
        f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()



















