


class StatusChangedListener():
    @olympe.listen_event()
    def onStatusChanged(self, event, scheduler):
        print_event(event)


