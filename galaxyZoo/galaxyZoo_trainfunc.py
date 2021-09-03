import torch
import time

def train_model(model, num_epochs, criterion, optimizer, scheduler, print_every=1, is_for_inception=False):
    """
    Train the model
    Args:
        model: Pytorch neural model
        num_epochs: number of epochs to train
        criterion: the loss function object
        optimizer: the optimizer
        scheduler: the learning rate decay scheduler
        print_every: print the information every X epochs
        is_for_inception: True if the model is an inception model
    """

    for epoch in range(num_epochs):
        # time of start
        epoch_start_time = time.time()

        """
        Train
        """
        model.train()

        epoch_train_cum_loss = 0.0
        epoch_train_cum_corrects = 0

        for images, labels in train_loader:
            images = images.to(device)
            labels = labels.long().to(device)

            optimizer.zero_grad()

            if is_for_inception:
                pred_logits, aux_outputs = model(images)
                loss = criterion(pred_logits, labels) + 0.4 * criterion(aux_outputs, labels)
            else:
                pred_logits = model(images)
                loss = criterion(pred_logits, labels)

            _, pred_classes = torch.max(pred_logits.detach(), dim=1)
            pred_classes = pred_classes.long()

            epoch_train_cum_loss += loss.item() * images.size(0)
            epoch_train_cum_corrects += torch.sum(pred_classes == labels.data)

            loss.backward()
            optimizer.step()

        """
        Eval
        """
        model.eval()

        epoch_test_cum_loss = 0.0
        epoch_test_cum_corrects = 0

        for images, labels in test_loader:
            images = images.to(device)
            labels = labels.long().to(device)

            with torch.no_grad():
                pred_logits = model(images)
                _, pred_classes = torch.max(pred_logits.detach(), dim=1)
                loss = criterion(pred_logits, labels)

                epoch_test_cum_loss += loss.item() * images.size(0)
                epoch_test_cum_corrects += torch.sum(pred_classes == labels.data)

        scheduler.step()

        ## Calculate metrics
        train_loss = epoch_train_cum_loss / len(data_train)
        train_acc = epoch_train_cum_corrects / len(data_train)
        test_loss = epoch_test_cum_loss / len(data_test)
        test_acc = epoch_test_cum_corrects / len(data_test)

        epoch_end_time = time.time()
        epoch_time_used = epoch_end_time - epoch_start_time

        ## Print metrics
        if (epoch + 1) % print_every == 0:
            print("Epoch {}/{}\tTrain loss: {:.4f}\tTrain acc: {:.3f}\tTest loss: {:.4f}\tTest acc: {:.3f}\tTime: {:.0f}m {:.0f}s".format(
                    epoch + 1, num_epochs, train_loss, train_acc, test_loss, test_acc, epoch_time_used // 60,
                    epoch_time_used % 60))