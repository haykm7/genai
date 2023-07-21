class Resource:
    def __init__(self, name, manufacturer, total, allocated):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = allocated

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"Resource(name='{self._name}', manufacturer='{self._manufacturer}', total={self._total}, allocated={self._allocated})"

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    def claim(self, n):
        if n <= self._total - self._allocated:
            self._allocated += n
            print(f"Claimed {n} {self._name}(s).")
        else:
            print("Insufficient inventory.")

    def freeup(self, n):
        if n <= self._allocated:
            self._allocated -= n
            print(f"Freed up {n} {self._name}(s).")
        else:
            print("Invalid operation. Cannot free up more resources than allocated.")

    def died(self, n):
        if n <= self._total:
            self._total -= n
            if n <= self._allocated:
                self._allocated -= n
            print(f"Removed {n} {self._name}(s) permanently.")
        else:
            print("Invalid operation. Cannot remove more resources than available.")

    def purchased(self, n):
        self._total += n
        print(f"Purchased {n} new {self._name}(s).")

    @property
    def category(self):
        return self.__class__.__name__.lower()


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_GB = capacity_GB

    @property
    def capacity_GB(self):
        return self._capacity_GB


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._size = size
        self._rpm = rpm

    def __repr__(self):
        return f"HDD(name='{self._name}', manufacturer='{self._manufacturer}', total={self._total}, allocated={self._allocated}, capacity_GB={self._capacity_GB}, size='{self._size}', rpm={self._rpm})"

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm


class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._interface = interface

    def __repr__(self):
        return f"SSD(name='{self._name}', manufacturer='{self._manufacturer}', total={self._total}, allocated={self._allocated}, capacity_GB={self._capacity_GB}, interface='{self._interface}')"

    @property
    def interface(self):
        return self._interface


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores):
        super().__init__(name, manufacturer, total, allocated)
        self._cores = cores

    def __repr__(self):
        return f"CPU(name='{self._name}', manufacturer='{self._manufacturer}', total={self._total}, allocated={self._allocated}, cores={self._cores})"

    @property
    def cores(self):
        return self._cores


cpu = CPU("Intel Core i9-9900K", "Intel", 10, 2, 8)
print(cpu)  # Output: Intel Core i9-9900K
print(cpu.category)  # Output: cpu

cpu.claim(1)  # Output: Claimed 1 Intel Core i9-9900K(s).
cpu.freeup(1)  # Output: Freed up 1 Intel Core i9-9900K(s).
cpu.died(1)  # Output: Removed 1 Intel Core i9-9900K(s) permanently.
cpu.purchased(5)  # Output: Purchased 5 new Intel Core i9-9900K(s).

hdd = HDD("Seagate Barracuda", "Seagate", 20, 5, 2000, "3.5\"", 7200)
print(hdd)  # Output: HDD(name='Seagate Barracuda', manufacturer='Seagate', total=20, allocated=5, capacity_GB=2000, size='3.5"', rpm=7200)
print(hdd.category)  # Output: hdd

ssd = SSD("Samsung 970 EVO", "Samsung", 15, 3, 500, "PCIe NVMe 3.0 x4")
print(ssd)  # Output: Samsung 970 EVO
print(ssd.category)  # Output: ssd

