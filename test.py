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
