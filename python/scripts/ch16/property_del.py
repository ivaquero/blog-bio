class BlackKnight:
    def __init__(self):
        self.members = ["an arm", "another arm", "a leg", "another leg"]
        self.phrases = [
            "'Tis but a scratch.",
            "It's just a flesh wound.",
            "I'm invincible!",
            "All right, we'll call it a draw.",
        ]

    @property
    def member(self):
        print("next member is:")
        return self.members[0]

    @member.deleter
    def member(self):
        print(f"BLACK KNIGHT (loses {self.members.pop(0)})\n-- {self.phrases.pop(0)}")


knight = BlackKnight()
knight.member
# next member is:
# 'an arm'
del knight.member
# BLACK KNIGHT (loses an arm)
# -- 'Tis but a scratch.
del knight.member
# BLACK KNIGHT (loses another arm)
# -- It's just a flesh wound.
del knight.member
# BLACK KNIGHT (loses a leg)
# -- I'm invincible!
del knight.member
# BLACK KNIGHT (loses another leg)
# -- All right, we'll call it a draw.
