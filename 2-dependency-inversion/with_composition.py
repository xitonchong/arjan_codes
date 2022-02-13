''' very advanced employee management system. '''

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class Contract(ABC):
    ''' represent a contract anda payment process for a particular employee.'''
    
    @abstractmethod
    def get_payment(self) -> float:
        ''' compute how much to pay an employee under this contract. '''


class Commission(ABC):
    ''' represents a commision payment process'''

    @abstractmethod
    def get_payment(self) -> float:
        ''' returns the commiison to be paid out.'''

@dataclass
class ContractCommission(Commission):
    '''represent a commision payemnt process based on the number of contracts landed '''
    
    commision: float = 100
    contracts_landed: int = 0
    
    def get_payment(self) -> float:
        ''' returns the commision to be paid out'''
        return self.commision * self.contracts_landed


@dataclass
class Employee:
    name: str
    id: str
    contract: Contract
    commision: Optional[Commission] = None
    
    def compute_pay(self):
        payout = self.contract.get_payment()
        if self.commision is not None:
            payout += self.commision.get_payment()
        return payout
        
@dataclass
class HourlyContract(Contract):
    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost


@dataclass
class SalariedContract(Contract):
    ''' contract type for an emplyee being paid a monthly salary'''
    monthly_salary: float
    percentage: float = 1
    
    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class FreeLancerContract(Contract):
    ''' contract type for a  freelancer (paid on an hourly basis)'''
    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""


    def get_payment(self):
        return self.pay_rate * self.hours_worked 



def main() -> None:
    ''' main function'''
    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=123232, contract=henry_contract)
    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours "
        f" and earned ${henry.compute_pay()}."
    )
    
    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed=10)
    sarah = Employee(name="Sarah", id=458495, contract=sarah_contract, 
                    commision=sarah_commission)
    print(
        f"{sarah.name} landed {sarah.commision.contracts_landed} contracts "
        f" and earned ${sarah.compute_pay()}.")


if __name__ == '__main__':
    main()







