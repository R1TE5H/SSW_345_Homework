from abc import ABC, abstractmethod

class SM(ABC):
    state = 0
    startState = 0

    def start(self):
        self.state = self.startState

    # step returns the next output.
    # getNextValues returns (nextState, nextOutput)
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]

    def run(self, n=10):
        return self.transduce([None] * n)

    # by default getNextValues assumes that
    # the output is the next state.
    def getNextValues(self, state, inp):
        nextState = self.getNextState(state, inp)
        return (nextState, nextState)

    @abstractmethod
    def getNextState(self, state, inp):
        pass

class VendingMachine(SM):
    startState = 0
    price = 75
    
    def getNextValues(self, state, inp):
   
        inp = inp.lower()

        # Handling cancellation
        if inp == "cancel":
            return (0, f"Cancelled. Returning ${state / 100:.2f}")

        # Handling money inputs    
        if inp == "nickel":
            state += 5
        elif inp == "dime":
            state += 10
        elif inp == "quarter":
            state += 25
        elif inp == "dollar":
            state += 100

        # Handling purchase
        if state >= self.price:
            change = state - self.price
            return (0, f"Inserted ${state / 100:.2f}. Drink dispensed. Change: ${change / 100:.2f}")
        else:
            return (state, f"Inserted ${state / 100:.2f}. Waiting for more money.")
            
    def run(self, inputs):
        return self.transduce(inputs)
    
    def getNextState(self, state, inp):
        return state

# Test the vending machine with a sequence of inputs
vendingMachine = VendingMachine()

inputs = ['quarter', 'quarter', 'quarter']
print(vendingMachine.run(inputs))  

inputs = ['quarter', 'cancel']
print(vendingMachine.run(inputs))

inputs = ['dime', 'dollar']
print(vendingMachine.run(inputs))