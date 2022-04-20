import torch
import matplotlib.pyplot as plt


def get_line(lr=1e-2, final_div_factor=0.5, pct_start=0.15, div_factor=5, steps=50000):
    net = torch.nn.Linear(1, 1)
    optim = torch.optim.AdamW(net.parameters(), lr=lr)

    scheduler = torch.optim.lr_scheduler.OneCycleLR(
            optim, lr, steps,
            pct_start=pct_start,
            div_factor=div_factor,
            final_div_factor=final_div_factor,
            cycle_momentum=True)

    for _ in range(steps):
        optim.step()
        scheduler.step()

        yield scheduler.get_last_lr()[0]


def main():
    ARGS = [
        dict(lr=1e-2, final_div_factor=.1, pct_start=0.2, div_factor=10, steps=25001),
        dict(lr=1e-2, final_div_factor=.2, pct_start=0.2, div_factor=10, steps=25001),
        dict(lr=1e-2, final_div_factor=.5, pct_start=0.2, div_factor=10, steps=25001),
        dict(lr=1e-2, final_div_factor=1, pct_start=0.2, div_factor=10, steps=25001),
        dict(lr=1e-2, final_div_factor=2, pct_start=0.2, div_factor=10, steps=25001),
        dict(lr=1e-2, final_div_factor=10, pct_start=0.2, div_factor=10, steps=25001),
        dict(lr=1e-2, final_div_factor=100, pct_start=0.2, div_factor=10, steps=25001),
    ]

    for i, args in enumerate(ARGS):
        points = list(get_line(**args))

        plt.plot(points, label=str(args['final_div_factor']))

    plt.yscale('log')
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()

