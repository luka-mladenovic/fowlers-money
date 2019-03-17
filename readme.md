# Money

A basic example implementation of the [Fowler's Money pattern](https://martinfowler.com/eaaCatalog/money.html). The library performs money operations using the currency's smallest unit to prevent rounding errors.

```python
from money.money import Money
from money.currency import Currency

euro = Money(100, Currency('EUR'))
ten_euro = euro + Money(900, Currency('EUR'))

print(ten_euro.amount) //1000

share = ten_euro.allocate([1,1,1])

print(share[0].amount) //334
print(share[1].amount) //333
print(share[2].amount) //333
```



## Usage

#### Instantiation

Money amount is represented in currency's smallest units / cents. (e.g. 100 for 1 euro).

```python
euro = Money(100, Currency('EUR'))

print(euro.amount) // 100
```



## Operations

- add

- subtract

- multiply


### Add

Sum amount of two money objects.  Addition must be made between objects with the same currency.

```python
five_euro = Money(500, Currency('EUR'))

ten_euro = five_euro + five_euro
```



### Subtract

Subtract amount of two money objects.  Subtraction must be made between objects with the same currency.

```python
five_euro = Money(500, Currency('EUR'))

zero_euro = five_euro - five_euro
```



### Multiply

Multiply amount with given multiplier. 

```python
five_euro = Money(500, Currency('EUR'))

ten_euro = five_euro * 2
```



## Allocation

- Allocate



### Allocate

Split money amount according to provided ratios. Remaining amount is distributed to shares with the biggest ratios.

```python
ten_euro = Money(1000, Currency('EUR'))

allocate = ten_euro.allocate([1,1,1])

print(allocate[0].amount) //334
print(allocate[1].amount) //333
print(allocate[2].amount) //333
```



## Comparison

- Equals
- GreaterThan
- GreaterThanOrEqual
- LessThan
- LessThanOrEqual



Compare amount of two money objects. All comparisons expect the `equals` must be made between objects with the same currency.

```python
five_euro = Money(500, Currency('EUR'))
ten_euro = Money(1000, Currency('EUR'))

five_euro == ten_euro // false
five_euro > ten_euro // false
five_euro >= ten_euro // false
five_euro < ten_euro // true
five_euro <= ten_euro // true
```



## License

The MIT License (MIT). See the license file for more information.