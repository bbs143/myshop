from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Coupon
from .forms import CouponApplyForm
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session[settings.COUPON_SESSION_ID] = coupon.id
        except ObjectDoesNotExist:
            request.session[settings.COUPON_SESSION_ID] = None

    return redirect('cart:cart_detail')
