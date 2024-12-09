from app.models.member import Member

class MemberService:
    def __init__(self):
        self.members = {}
        self.counter = 1

    def create_member(self, name):
        member = Member(self.counter, name)
        self.members[self.counter] = member
        self.counter += 1
        return member

    def get_members(self):
        return list(self.members.values())

    def get_member(self, member_id):
        return self.members.get(member_id)

    def update_member(self, member_id, name):
        if member_id in self.members:
            self.members[member_id].name = name
            return self.members[member_id]
        return None

    def delete_member(self, member_id):
        return self.members.pop(member_id, None)