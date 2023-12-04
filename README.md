# Пример Cocotb
## Опсиание теста
В тесте используется простой счетчик, находящийся в файле counter.v:
```verilog
module counter(out, clk, reset);

  parameter WIDTH = 8;

  output [WIDTH-1: 0] out;
  input 	       clk, reset;

  reg [WIDTH-1: 0]   out;
  wire 	       clk, reset;

  always @(posedge clk or posedge reset)
    if (reset)
      out <= 0;
    else
      out <= out + 1;

endmodule // counter
```

Его testbench сделать с использованием Cocotb как:
```python
import cocotb
from cocotb.triggers import Timer


async def generate_clock(dut):
    for cycle in range(100):
        dut.clk.value = 0
        await Timer(0.5, units="ns")
        dut.clk.value = 1
        await Timer(0.5, units="ns")


@cocotb.test()
async def test(dut):
    dut.out.value = 0
    await cocotb.start(generate_clock(dut))
    await generate_clock(dut)

    await Timer(10, units="ns")

    assert dut.out.value == 100
```

Функция generate_clock переключает clk каждые 0.5 нс, чтобы обеспечить период 1 нс. Сначала выставляется нулевое значение счетчика, после чего запускается 100 периодов clock и проверяется, что значение счетчика также равно 100.

## Makefile
```bash
## defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/counter.v
## use VHDL_SOURCES for VHDL files

## TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = counter

## MODULE is the basename of the Python test file
MODULE = test

## include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
```

## make_and_gtk
Скрипт make_and_gtk собирает проект и запускает gtkwave по результатам.

## Результат
![](result.png)

## Запуск теста
```bash
./make_and_gtk
```

# Запуск теста matrix_multiplier
## Вывод в консоль:
```
    20.00ns INFO     cocotb.matrix_multiplier           Test multiplication operations
    40.00ns INFO     cocotb.matrix_multiplier           0 / 3000
  2040.00ns INFO     cocotb.matrix_multiplier           100 / 3000
  4040.00ns INFO     cocotb.matrix_multiplier           200 / 3000
  6040.00ns INFO     cocotb.matrix_multiplier           300 / 3000
  8040.00ns INFO     cocotb.matrix_multiplier           400 / 3000
 10040.00ns INFO     cocotb.matrix_multiplier           500 / 3000
 12040.00ns INFO     cocotb.matrix_multiplier           600 / 3000
 14040.00ns INFO     cocotb.matrix_multiplier           700 / 3000
 16040.00ns INFO     cocotb.matrix_multiplier           800 / 3000
 18040.00ns INFO     cocotb.matrix_multiplier           900 / 3000
 20040.00ns INFO     cocotb.matrix_multiplier           1000 / 3000
 22040.00ns INFO     cocotb.matrix_multiplier           1100 / 3000
 24040.00ns INFO     cocotb.matrix_multiplier           1200 / 3000
 26040.00ns INFO     cocotb.matrix_multiplier           1300 / 3000
 28040.00ns INFO     cocotb.matrix_multiplier           1400 / 3000
 30040.00ns INFO     cocotb.matrix_multiplier           1500 / 3000
 32040.00ns INFO     cocotb.matrix_multiplier           1600 / 3000
 34040.00ns INFO     cocotb.matrix_multiplier           1700 / 3000
 36040.00ns INFO     cocotb.matrix_multiplier           1800 / 3000
 38040.00ns INFO     cocotb.matrix_multiplier           1900 / 3000
 40040.00ns INFO     cocotb.matrix_multiplier           2000 / 3000
 42040.00ns INFO     cocotb.matrix_multiplier           2100 / 3000
 44040.00ns INFO     cocotb.matrix_multiplier           2200 / 3000
 46040.00ns INFO     cocotb.matrix_multiplier           2300 / 3000
 48040.00ns INFO     cocotb.matrix_multiplier           2400 / 3000
 50040.00ns INFO     cocotb.matrix_multiplier           2500 / 3000
 52040.00ns INFO     cocotb.matrix_multiplier           2600 / 3000
 54040.00ns INFO     cocotb.matrix_multiplier           2700 / 3000
 56040.00ns INFO     cocotb.matrix_multiplier           2800 / 3000
 58040.00ns INFO     cocotb.matrix_multiplier           2900 / 3000
 60030.00ns INFO     cocotb.regression                  multiply_test passed
 60030.00ns INFO     cocotb.regression                  **********************************************************************************************
                                                        ** TEST                                  STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                                                        **********************************************************************************************
                                                        ** test_matrix_multiplier.multiply_test   PASS       60030.00           5.95      10093.67  **
                                                        **********************************************************************************************
                                                        ** TESTS=1 PASS=1 FAIL=0 SKIP=0                      60030.00           6.04       9940.75  **
                                                        **********************************************************************************************
```