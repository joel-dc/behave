from behave import *

class Example:
    def __init__(self):
        self._counter = 0

    def count(self):
        self._counter += 1
        return self._counter

    def clear_counter(self):
        self._counter = 0
        return self._counter

    def get_value(self):
        return self._counter

    def set_counter(self, val):
        self._counter = int(val)

    def hello(self, name):
        return "Hello, " + name

    def hello_world(self):
        return "hello world"

class ExampleTest:
    def __init__(self):
        self._counters = []

    @given('a name')
    @when('approached by others')
    def step_pass(self):
        pass

    @then('greet appropriately by saying hello')
    def assertHello(self):
        example = Example()
        for row in self.table:
            assert example.hello(row['name']) == row['greeting']

    @given('an initialized counter')
    def setCounters(self):
        self._counters = []
        for row in self.table:
            counter = Example()
            counter.set_counter(row['val'])
            self._counters.append(counter)

    @when('the counter is incremented')
    def incrCounters(self):
        for counter in self._counters:
            counter.count()

    @then('the counter should be incremented')
    def assertIncr(self):
        expected = []
        vals = []

        for row in self.table:
            expected.append(int(row['incr']))

        for counter in self._counters:
            vals.append(counter.get_value() )

        assert 0 is cmp(expected, vals)