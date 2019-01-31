class CreateUpdateMixin(object):

    def create(self, validated_data):
        if 'created_by' not in self.context['request'].POST:
            validated_data['created_by'] = self.context['request'].user

        return super(CreateUpdateMixin, self).create(validated_data)