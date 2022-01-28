import torch
import matplotlib.pyplot as plt


def main(lr=2e-3, min_lr=1e-4, pct_start=0.25, div_factor=10, steps=50000):
    net = torch.nn.Linear(1, 1)
    optim = torch.optim.SGD(net.parameters(), lr=lr)

    scheduler = torch.optim.lr_scheduler.OneCycleLR(
            optim, lr, steps,
            pct_start=pct_start,
            div_factor=div_factor,
            final_div_factor=(lr / div_factor) / min_lr)

    for _ in range(steps):
        optim.step()
        scheduler.step()

        yield scheduler.get_last_lr()


if __name__ == '__main__':
    points = list(main())

    plt.plot(points)
    plt.yscale('log')
    plt.show()
