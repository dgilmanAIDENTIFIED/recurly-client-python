#
# This file is automatically created by Recurly's OpenAPI generation process
# and thus any edits you make by hand will be lost. If you wish to make a
# change to this file, please create a Github issue explaining the changes you
# need and we will usher them to the appropriate places.
from .resource import Resource
import datetime


class Site(Resource):
    """
    Attributes
    ----------
    address : Address
    created_at : datetime
        Created at
    deleted_at : datetime
        Deleted at
    id : str
        Site ID
    mode : str
        Mode
    settings : Settings
    subdomain : str
    updated_at : datetime
        Updated at
    """

    schema = {
        "address": "Address",
        "created_at": datetime,
        "deleted_at": datetime,
        "id": str,
        "mode": str,
        "settings": "Settings",
        "subdomain": str,
        "updated_at": datetime,
    }


class Address(Resource):
    """
    Attributes
    ----------
    city : str
        City
    country : str
        Country, 2-letter ISO code.
    first_name : str
        First name
    last_name : str
        Last name
    phone : str
        Phone number
    postal_code : str
        Zip or postal code.
    region : str
        State or province.
    street1 : str
        Street 1
    street2 : str
        Street 2
    """

    schema = {
        "city": str,
        "country": str,
        "first_name": str,
        "last_name": str,
        "phone": str,
        "postal_code": str,
        "region": str,
        "street1": str,
        "street2": str,
    }


class Settings(Resource):
    """
    Attributes
    ----------
    accepted_currencies : :obj:`list` of :obj:`str`
    billing_address_requirement : str
        - full:      Full Address (Street, City, State, Postal Code and Country)
        - streetzip: Street and Postal Code only
        - zip:       Postal Code only
        - none:      No Address
    default_currency : str
        The default 3-letter ISO 4217 currency code.
    """

    schema = {
        "accepted_currencies": list,
        "billing_address_requirement": str,
        "default_currency": str,
    }


class Error(Resource):
    """
    Attributes
    ----------
    message : str
        Message
    params : :obj:`list` of :obj:`dict`
        Parameter specific errors
    type : str
        Type
    """

    schema = {"message": str, "params": list, "type": str}


class Account(Resource):
    """
    Attributes
    ----------
    address : Address
    billing_info : BillingInfo
    cc_emails : str
        Additional email address that should receive account correspondence. These should be separated only by commas. These CC emails will receive all emails that the `email` field also receives.
    code : str
        The unique identifier of the account. This cannot be changed once the account is created.
    company : str
    created_at : datetime
        When the account was created.
    deleted_at : datetime
        If present, when the account was last marked inactive.
    email : str
        The email address used for communicating with this customer. The customer will also use this email address to log into your hosted account management pages. This value does not need to be unique.
    first_name : str
    hosted_login_token : str
        The unique token for automatically logging the account in to the hosted management pages. You may automatically log the user into their hosted management pages by directing the user to: `https://{subdomain}.recurly.com/account/{hosted_login_token}`.
    id : str
    last_name : str
    shipping_addresses : :obj:`list` of :obj:`ShippingAddress`
        The shipping addresses on the account.
    state : str
        Accounts can be either active or inactive.
    tax_exempt : bool
        The tax status of the account. `true` exempts tax on the account, `false` applies tax on the account.
    updated_at : datetime
        When the account was last changed.
    username : str
        A secondary value for the account.
    vat_number : str
        The VAT number of the account (to avoid having the VAT applied). This is only used for manually collected invoices.
    """

    schema = {
        "address": "Address",
        "billing_info": "BillingInfo",
        "cc_emails": str,
        "code": str,
        "company": str,
        "created_at": datetime,
        "deleted_at": datetime,
        "email": str,
        "first_name": str,
        "hosted_login_token": str,
        "id": str,
        "last_name": str,
        "shipping_addresses": ["ShippingAddress"],
        "state": str,
        "tax_exempt": bool,
        "updated_at": datetime,
        "username": str,
        "vat_number": str,
    }


class ShippingAddress(Resource):
    """
    Attributes
    ----------
    account_id : str
        Account ID
    city : str
    company : str
    country : str
        Country, 2-letter ISO code.
    created_at : datetime
        Created at
    email : str
    first_name : str
    id : str
        Shipping Address ID
    last_name : str
    nickname : str
    phone : str
    postal_code : str
        Zip or postal code.
    region : str
        State or province.
    street1 : str
    street2 : str
    updated_at : datetime
        Updated at
    vat_number : str
    """

    schema = {
        "account_id": str,
        "city": str,
        "company": str,
        "country": str,
        "created_at": datetime,
        "email": str,
        "first_name": str,
        "id": str,
        "last_name": str,
        "nickname": str,
        "phone": str,
        "postal_code": str,
        "region": str,
        "street1": str,
        "street2": str,
        "updated_at": datetime,
        "vat_number": str,
    }


class BillingInfo(Resource):
    """
    Attributes
    ----------
    account_id : str
    address : Address
    company : str
    created_at : datetime
        When the billing information was created.
    first_name : str
    fraud : FraudInfo
        Most recent fraud result.
    id : str
    last_name : str
    payment_method : PaymentMethod
    updated_at : datetime
        When the billing information was last changed.
    updated_by : BillingInfoUpdatedBy
    valid : bool
    vat_number : str
        Customer's VAT number (to avoid having the VAT applied). This is only used for automatically collected invoices.
    """

    schema = {
        "account_id": str,
        "address": "Address",
        "company": str,
        "created_at": datetime,
        "first_name": str,
        "fraud": "FraudInfo",
        "id": str,
        "last_name": str,
        "payment_method": "PaymentMethod",
        "updated_at": datetime,
        "updated_by": "BillingInfoUpdatedBy",
        "valid": bool,
        "vat_number": str,
    }


class PaymentMethod(Resource):
    """
    Attributes
    ----------
    account_type : str
        The bank account type. Only present for ACH payment methods.
    billing_agreement_id : str
        Billing Agreement identifier. Only present for Amazon or Paypal payment methods.
    card_type : str
        Visa, MasterCard, American Express, Discover, JCB, etc.
    exp_month : int
        Expiration month.
    exp_year : int
        Expiration year.
    first_six : str
        Credit card number's first six digits.
    last_four : str
        Credit card number's last four digits. Will refer to bank account if payment method is ACH.
    routing_number : str
        The bank account's routing number. Only present for ACH payment methods.
    routing_number_bank : str
        The bank name of this routing number.
    """

    schema = {
        "account_type": str,
        "billing_agreement_id": str,
        "card_type": str,
        "exp_month": int,
        "exp_year": int,
        "first_six": str,
        "last_four": str,
        "routing_number": str,
        "routing_number_bank": str,
    }


class FraudInfo(Resource):
    """
    Attributes
    ----------
    decision : str
        Kount decision
    risk_rules_triggered : dict
        Kount rules
    score : int
        Kount score
    """

    schema = {"decision": str, "risk_rules_triggered": dict, "score": int}


class BillingInfoUpdatedBy(Resource):
    """
    Attributes
    ----------
    country : str
        Country of IP address, if known by Recurly.
    ip : str
        Customer's IP address when updating their billing information.
    """

    schema = {"country": str, "ip": str}


class ErrorMayHaveTransaction(Resource):
    """
    Attributes
    ----------
    message : str
        Message
    params : :obj:`list` of :obj:`dict`
        Parameter specific errors
    transaction_error : TransactionError
        This is only included on errors with `type=transaction`.
    type : str
        Type
    """

    schema = {
        "message": str,
        "params": list,
        "transaction_error": "TransactionError",
        "type": str,
    }


class TransactionError(Resource):
    """
    Attributes
    ----------
    category : str
        Category
    code : str
        Code
    merchant_advice : str
        Merchant message
    message : str
        Customer message
    transaction_id : str
        Transaction ID
    """

    schema = {
        "category": str,
        "code": str,
        "merchant_advice": str,
        "message": str,
        "transaction_id": str,
    }


class AccountAcquisition(Resource):
    """
    Attributes
    ----------
    account : AccountMini
    campaign : str
        An arbitrary identifier for the marketing campaign that led to the acquisition of this account.
    channel : str
        The channel through which the account was acquired.
    cost : AccountAcquisitionCost
    created_at : datetime
        When the account acquisition data was created.
    id : str
    subchannel : str
        An arbitrary subchannel string representing a distinction/subcategory within a broader channel.
    updated_at : datetime
        When the account acquisition data was last changed.
    """

    schema = {
        "account": "AccountMini",
        "campaign": str,
        "channel": str,
        "cost": "AccountAcquisitionCost",
        "created_at": datetime,
        "id": str,
        "subchannel": str,
        "updated_at": datetime,
    }


class AccountAcquisitionCost(Resource):
    """
    Attributes
    ----------
    amount : float
        The amount of the corresponding currency used to acquire the account.
    currency : str
        3-letter ISO 4217 currency code.
    """

    schema = {"amount": float, "currency": str}


class AccountMini(Resource):
    """
    Attributes
    ----------
    code : str
        The unique identifier of the account.
    email : str
        The email address used for communicating with this customer.
    first_name : str
    id : str
    last_name : str
    """

    schema = {"code": str, "email": str, "first_name": str, "id": str, "last_name": str}


class AccountBalance(Resource):
    """
    Attributes
    ----------
    account : AccountMini
    balances : :obj:`list` of :obj:`AccountBalanceAmount`
    past_due : bool
    """

    schema = {
        "account": "AccountMini",
        "balances": ["AccountBalanceAmount"],
        "past_due": bool,
    }


class AccountBalanceAmount(Resource):
    """
    Attributes
    ----------
    amount : float
        Total amount the account is past due.
    currency : str
        3-letter ISO 4217 currency code.
    """

    schema = {"amount": float, "currency": str}


class BooleanResponse(Resource):
    """
    Attributes
    ----------
    success : bool
    """

    schema = {"success": bool}


class CouponRedemption(Resource):
    """
    Attributes
    ----------
    account : AccountMini
        The Account on which the coupon was applied.
    coupon : Coupon
    created_at : datetime
        Created at
    currency : str
        3-letter ISO 4217 currency code.
    discounted : float
        The amount that was discounted upon the application of the coupon, formatted with the currency.
    id : str
        Coupon Redemption ID
    removed_at : datetime
        The date and time the redemption was removed from the account (un-redeemed).
    state : str
        Coupon Redemption state
    updated_at : datetime
        Last updated at
    """

    schema = {
        "account": "AccountMini",
        "coupon": "Coupon",
        "created_at": datetime,
        "currency": str,
        "discounted": float,
        "id": str,
        "removed_at": datetime,
        "state": str,
        "updated_at": datetime,
    }


class Coupon(Resource):
    """
    Attributes
    ----------
    applies_to_all_plans : bool
        The coupon is valid for all plans if true. If false then `plans` and `plans_names` will list the applicable plans.
    applies_to_non_plan_charges : bool
        The coupon is valid for one-time, non-plan charges if true.
    code : str
        The code the customer enters to redeem the coupon.
    coupon_type : str
        Whether the coupon is "single_code" or "bulk". Bulk coupons will require a `unique_code_template` and will generate unique codes through the `/generate` endpoint.
    created_at : datetime
        Created at
    discount : CouponDiscount
    duration : str
        - "single_use" coupons applies to the first invoice only.
        - "temporal" coupons will apply to invoices for the duration determined by the `temporal_unit` and `temporal_amount` attributes.
    expired_at : datetime
        The date and time the coupon was expired early or reached its `max_redemptions`.
    free_trial_amount : int
        Sets the duration of time the `free_trial_unit` is for.
    free_trial_unit : str
        Description of the unit of time the coupon is for. Used with `free_trial_amount` to determine the duration of time the coupon is for.
    hosted_page_description : str
        This description will show up when a customer redeems a coupon on your Hosted Payment Pages, or if you choose to show the description on your own checkout page.
    id : str
        Coupon ID
    invoice_description : str
        Description of the coupon on the invoice.
    max_redemptions : int
        A maximum number of redemptions for the coupon. The coupon will expire when it hits its maximum redemptions.
    max_redemptions_per_account : int
        Redemptions per account is the number of times a specific account can redeem the coupon. Set redemptions per account to `1` if you want to keep customers from gaming the system and getting more than one discount from the coupon campaign.
    name : str
        The internal name for the coupon.
    plans : :obj:`list` of :obj:`PlanMini`
        Plans
    plans_names : :obj:`list` of :obj:`str`
        TODO
    redeem_by : datetime
        The date and time the coupon will expire and can no longer be redeemed. Time is always 11:59:59, the end-of-day Pacific time.
    redemption_resource : str
        Whether the discount is for all eligible charges on the account, or only a specific subscription.
    state : str
        Indicates if the coupon is redeemable, and if it is not, why.
    temporal_amount : int
        If `duration` is "temporal" than `temporal_amount` is an integer which is multiplied by `temporal_unit` to define the duration that the coupon will be applied to invoices for.
    temporal_unit : str
        If `duration` is "temporal" than `temporal_unit` is multiplied by `temporal_amount` to define the duration that the coupon will be applied to invoices for.
    unique_coupon_codes_count : int
        When this number reaches `max_redemptions` the coupon will no longer be redeemable.
    updated_at : datetime
        Last updated at
    """

    schema = {
        "applies_to_all_plans": bool,
        "applies_to_non_plan_charges": bool,
        "code": str,
        "coupon_type": str,
        "created_at": datetime,
        "discount": "CouponDiscount",
        "duration": str,
        "expired_at": datetime,
        "free_trial_amount": int,
        "free_trial_unit": str,
        "hosted_page_description": str,
        "id": str,
        "invoice_description": str,
        "max_redemptions": int,
        "max_redemptions_per_account": int,
        "name": str,
        "plans": ["PlanMini"],
        "plans_names": list,
        "redeem_by": datetime,
        "redemption_resource": str,
        "state": str,
        "temporal_amount": int,
        "temporal_unit": str,
        "unique_coupon_codes_count": int,
        "updated_at": datetime,
    }


class PlanMini(Resource):
    """
    Attributes
    ----------
    code : str
        Unique code to identify the plan. This is used in Hosted Payment Page URLs and in the invoice exports.
    id : str
        Plan ID
    name : str
        This name describes your plan and will appear on the Hosted Payment Page and the subscriber's invoice.
    """

    schema = {"code": str, "id": str, "name": str}


class CouponDiscount(Resource):
    """
    Attributes
    ----------
    currencies : :obj:`list` of :obj:`CouponDiscountPricing`
    percent : int
    trial : CouponDiscountTrial
    type : str
    """

    schema = {
        "currencies": ["CouponDiscountPricing"],
        "percent": int,
        "trial": "CouponDiscountTrial",
        "type": str,
    }


class CouponDiscountPricing(Resource):
    """
    Attributes
    ----------
    amount : float
        Value of the fixed discount that this coupon applies.
    currency : str
        3-letter ISO 4217 currency code.
    """

    schema = {"amount": float, "currency": str}


class CouponDiscountTrial(Resource):
    """
    Attributes
    ----------
    length : int
        Trial length measured in the units specified by the sibling `unit` property
    unit : str
        Temporal unit of the free trial
    """

    schema = {"length": int, "unit": str}


class Invoice(Resource):
    """
    Attributes
    ----------
    account : AccountMini
    address : Address
    closed_at : datetime
        Date invoice was marked paid or failed.
    collection_method : str
        An automatic invoice means a corresponding transaction is run using the account's billing information at the same time the invoice is created. Manual invoices are created without a corresponding transaction. The merchant must enter a manual payment transaction or have the customer pay the invoice with an automatic method, like credit card, PayPal, Amazon, or ACH bank payment.
    created_at : datetime
        Created at
    currency : str
        3-letter ISO 4217 currency code.
    customer_notes : str
        This will default to the Customer Notes text specified on the Invoice Settings. Specify custom notes to add or override Customer Notes.
    discount : float
        Total discounts applied to this invoice.
    due : float
        The outstanding balance remaining on this invoice.
    due_at : datetime
        Date invoice is due. This is the date the net terms are reached.
    id : str
        Invoice ID
    line_items : InvoiceLineItems
        Line items are grouped by the role they play.
    net_terms : int
        Integer representing the number of days after an invoice's creation
        that the invoice will become past due. If an invoice's net terms are set
        to '0', it is due 'On Receipt' and will become past due 24 hours after it’s
        created. If an invoice is due net 30, it will become past due at 31 days
        exactly.
    number : str
        If VAT taxation and the Country Invoice Sequencing feature are enabled, invoices will have country-specific invoice numbers for invoices billed to EU countries (ex: FR1001). Non-EU invoices will continue to use the site-level invoice number sequence.
    paid : float
        The total amount of successful payments transaction on this invoice.
    po_number : str
        For manual invoicing, this identifies the PO number associated with the subscription.
    previous_invoice_id : str
        On refund invoices, this value will exist and show the invoice ID of the purchase invoice the refund was created from.
    state : str
        Invoice state
    subscription_id : str
        If the invoice is charging or refunding for a subscription, this is its ID.
    subtotal : float
        The summation of charges, discounts, and credits, before tax.
    tax : float
        The total tax on this invoice.
    tax_info : TaxInfo
    terms_and_conditions : str
        This will default to the Terms and Conditions text specified on the Invoice Settings page in your Recurly admin. Specify custom notes to add or override Terms and Conditions.
    total : float
        The final total on this invoice. The summation of invoice charges, discounts, credits, and tax.
    transactions : :obj:`list` of :obj:`Transaction`
        Transactions
    type : str
        The original invoice will have a type of `purchase`. Any refunds or voids will create a negative invoice to cancel out the original. `line_item_refund` indicates that specific line items were refunded, while `open_amount_refund` only indicates money was refunded.
    updated_at : datetime
        Last updated at
    vat_number : str
        VAT registration number for the customer on this invoice. This will come from the VAT Number field in the Billing Info or the Account Info depending on your tax settings and the invoice collection method.
    vat_reverse_charge_notes : str
        VAT Reverse Charge Notes only appear if you have EU VAT enabled or are using your own Avalara AvaTax account and the customer is in the EU, has a VAT number, and is in a different country than your own. This will default to the VAT Reverse Charge Notes text specified on the Tax Settings page in your Recurly admin, unless custom notes were created with the original subscription.
    """

    schema = {
        "account": "AccountMini",
        "address": "Address",
        "closed_at": datetime,
        "collection_method": str,
        "created_at": datetime,
        "currency": str,
        "customer_notes": str,
        "discount": float,
        "due": float,
        "due_at": datetime,
        "id": str,
        "line_items": "InvoiceLineItems",
        "net_terms": int,
        "number": str,
        "paid": float,
        "po_number": str,
        "previous_invoice_id": str,
        "state": str,
        "subscription_id": str,
        "subtotal": float,
        "tax": float,
        "tax_info": "TaxInfo",
        "terms_and_conditions": str,
        "total": float,
        "transactions": ["Transaction"],
        "type": str,
        "updated_at": datetime,
        "vat_number": str,
        "vat_reverse_charge_notes": str,
    }


class TaxInfo(Resource):
    """
    Attributes
    ----------
    rate : float
        Rate
    region : str
        Provides the tax region applied on an invoice. For U.S. Sales Tax, this will be the 2 letter state code. For EU VAT this will be the 2 letter country code. For all country level tax types, this will display the regional tax, like VAT, GST, or PST.
    type : str
        Provides the tax type as "vat" for EU VAT, "usst" for U.S. Sales Tax, or the 2 letter country code for country level tax types like Canada, Australia, New Zealand, Israel, and all non-EU European countries.
    """

    schema = {"rate": float, "region": str, "type": str}


class InvoiceLineItems(Resource):
    """
    Attributes
    ----------
    applied_credits : :obj:`list` of :obj:`LineItem`
        Previous credits applied to this invoice. See their `original_line_item_id` to determine where the credit first originated.
    carryforwards : :obj:`list` of :obj:`LineItem`
        These charges can be ignored. They exist to consume any remaining credit balance. A new credit with the same amount will be created and placed back on the account.
    charges : :obj:`list` of :obj:`LineItem`
        New charges being billed for on this invoice.
    credits : :obj:`list` of :obj:`LineItem`
        Refund or proration credits. This portion of the invoice can be considered a credit memo.
    """

    schema = {
        "applied_credits": ["LineItem"],
        "carryforwards": ["LineItem"],
        "charges": ["LineItem"],
        "credits": ["LineItem"],
    }


class LineItem(Resource):
    """
    Attributes
    ----------
    account : AccountMini
    accounting_code : str
        Internal accounting code to help you reconcile your revenue to the correct ledger. Line items created as part of a subscription invoice will use the plan or add-on's accounting code, otherwise the value will only be present if you define an accounting code when creating the line item.
    add_on_code : str
        If the line item is a charge or credit for an add-on, this is its code.
    add_on_id : str
        If the line item is a charge or credit for an add-on this is its ID.
    amount : float
        `(quantity * unit_amount) - (discount + tax)`
    created_at : datetime
        When the line item was created.
    credit_applied : float
        The amount of credit from this line item that was applied to the invoice.
    currency : str
        3-letter ISO 4217 currency code.
    description : str
        Description that appears on the invoice. For subscription related items this will be filled in automatically.
    discount : float
        The discount applied to the line item.
    end_date : datetime
        If this date is provided, it indicates the end of a time range.
    id : str
        Line item ID
    invoice_id : str
        Once the line item has been invoiced this will be the invoice's ID.
    invoice_number : str
        Once the line item has been invoiced this will be the invoice's number. If VAT taxation and the Country Invoice Sequencing feature are enabled, invoices will have country-specific invoice numbers for invoices billed to EU countries (ex: FR1001). Non-EU invoices will continue to use the site-level invoice number sequence.
    origin : str
        A credit created from an original charge will have the value of the charge's origin.
    original_line_item_id : str
        The line item where the credit originated. Will only have a value if the line item is a credit created from a previous credit, or if the credit was created from a charge refund. For some older invoices this may reference a carryforward charge.
    original_line_item_invoice_id : str
        The invoice where the credit originated. Will only have a value if the line item is a credit created from a previous credit, or if the credit was created from a charge refund.
    plan_code : str
        If the line item is a charge or credit for a plan or add-on, this is the plan's code.
    plan_id : str
        If the line item is a charge or credit for a plan or add-on, this is the plan's ID.
    previous_line_item_id : str
        Will only have a value if the line item is a credit created from a previous credit, or if the credit was created from a charge refund.
    product_code : str
        For plan related line items this will be the plan's code, for add-on related line items it will be the add-on's code.
    quantity : int
        This number will be multiplied by the unit amount to compute the subtotal before any discounts or taxes.
    refund : bool
        Refund?
    refunded_quantity : int
        For refund charges, the quantity being refunded. For non-refund charges, the total quantity refunded (possibly over multiple refunds).
    shipping_address : ShippingAddress
    start_date : datetime
        If an end date is present, this is value indicates the beginning of a billing time range. If no end date is present it indicates billing for a specific date.
    state : str
        Pending line items are charges or credits on an account that have not been applied to an invoice yet. Invoiced line items will always have an `invoice_id` value.
    subscription_id : str
        If the line item is a charge or credit for a subscription, this is its ID.
    subtotal : float
        `quantity * unit_amount`
    tax : float
        The tax amount for the line item.
    tax_code : str
        Used by Avalara, Vertex, and Recurly’s EU VAT tax feature. The tax code values are specific to each tax system. If you are using Recurly’s EU VAT feature `P0000000` is `physical`, `D0000000` is `digital`, and an empty string is `unknown`.
    tax_exempt : bool
        `true` exempts tax on charges, `false` applies tax on charges. If not defined, then defaults to the Plan and Site settings. This attribute does not work for credits (negative line items). Credits are always applied post-tax. Pre-tax discounts should use the Coupons feature.
    taxable : bool
        `true` if the line item is taxable, `false` if it is not.
    type : str
        Charges are positive line items that debit the account. Credits are negative line items that credit the account.
    unit_amount : float
        Positive amount for a charge, negative amount for a credit.
    updated_at : datetime
        When the line item was last changed.
    uuid : str
        The UUID is useful for matching data with the CSV exports and building URLs into Recurly's UI.
    """

    schema = {
        "account": "AccountMini",
        "accounting_code": str,
        "add_on_code": str,
        "add_on_id": str,
        "amount": float,
        "created_at": datetime,
        "credit_applied": float,
        "currency": str,
        "description": str,
        "discount": float,
        "end_date": datetime,
        "id": str,
        "invoice_id": str,
        "invoice_number": str,
        "origin": str,
        "original_line_item_id": str,
        "original_line_item_invoice_id": str,
        "plan_code": str,
        "plan_id": str,
        "previous_line_item_id": str,
        "product_code": str,
        "quantity": int,
        "refund": bool,
        "refunded_quantity": int,
        "shipping_address": "ShippingAddress",
        "start_date": datetime,
        "state": str,
        "subscription_id": str,
        "subtotal": float,
        "tax": float,
        "tax_code": str,
        "tax_exempt": bool,
        "taxable": bool,
        "type": str,
        "unit_amount": float,
        "updated_at": datetime,
        "uuid": str,
    }


class Transaction(Resource):
    """
    Attributes
    ----------
    account : AccountMini
    amount : float
        Total transaction amount sent to the payment gateway.
    avs_check : str
        When processed, result from checking the overall AVS on the transaction.
    billing_address : Address
    collected_at : datetime
        Collected at, or if not collected yet, the time the transaction was created.
    created_at : datetime
        Created at
    currency : str
        3-letter ISO 4217 currency code.
    customer_message : str
        For declined (`success=false`) transactions, the message displayed to the customer.
    customer_message_locale : str
        Language code for the message
    cvv_check : str
        When processed, result from checking the CVV/CVC value on the transaction.
    gateway_approval_code : str
        Transaction approval code from the payment gateway.
    gateway_message : str
        Transaction message from the payment gateway.
    gateway_reference : str
        Transaction reference number from the payment gateway.
    gateway_response_code : str
        For declined transactions (`success=false`), this field lists the gateway error code.
    gateway_response_time : float
        Time, in seconds, for gateway to process the transaction.
    gateway_response_values : dict
        The values in this field will vary from gateway to gateway.
    id : str
        Transaction ID
    invoice : InvoiceMini
    invoice_id : str
        If this transaction pays (`type=payment`) for or refunds (`type=refund`) an invoice, this will be the invoice's ID. It will be null for verification (`type=verify`) transactions.
    ip_address_country : str
        IP address's country
    ip_address_v4 : str
        IP address provided when the billing information was collected:

        - When the customer enters billing information into the Recurly.js or Hosted Payment Pages, Recurly records the IP address.
        - When the merchant enters billing information using the API, the merchant may provide an IP address.
        - When the merchant enters billing information using the UI, no IP address is recorded.
    origin : str
        Describes how the transaction was triggered.
    original_transaction_id : str
        If this transaction is a refund (`type=refund`), this will be the ID of the original transaction on the invoice being refunded.
    payment_gateway : TransactionPaymentGateway
    payment_method : PaymentMethod
    refunded : bool
        Indicates if part or all of this transaction was refunded.
    status : str
        The current transaction status. Note that the status may change, e.g. a `pending` transaction may become `declined` or `success` may later become `void`.
    status_code : str
        Status code
    status_message : str
        For declined (`success=false`) transactions, the message displayed to the merchant.
    subscription_id : str
        If the transaction is charging or refunding for a subscription, this is its ID.
    success : bool
        Did this transaction complete successfully?
    type : str
        - `authorization` – verifies billing information and places a hold on money in the customer's account.
        - `capture` – captures funds held by an authorization and completes a purchase.
        - `purchase` – combines the authorization and capture in one transaction.
        - `refund` – returns all or a portion of the money collected in a previous transaction to the customer.
        - `verify` – a $0 or $1 transaction used to verify billing information which is immediately voided.
    uuid : str
        The UUID is useful for matching data with the CSV exports and building URLs into Recurly's UI.
    voided_at : datetime
        Voided at
    """

    schema = {
        "account": "AccountMini",
        "amount": float,
        "avs_check": str,
        "billing_address": "Address",
        "collected_at": datetime,
        "created_at": datetime,
        "currency": str,
        "customer_message": str,
        "customer_message_locale": str,
        "cvv_check": str,
        "gateway_approval_code": str,
        "gateway_message": str,
        "gateway_reference": str,
        "gateway_response_code": str,
        "gateway_response_time": float,
        "gateway_response_values": dict,
        "id": str,
        "invoice": "InvoiceMini",
        "invoice_id": str,
        "ip_address_country": str,
        "ip_address_v4": str,
        "origin": str,
        "original_transaction_id": str,
        "payment_gateway": "TransactionPaymentGateway",
        "payment_method": "PaymentMethod",
        "refunded": bool,
        "status": str,
        "status_code": str,
        "status_message": str,
        "subscription_id": str,
        "success": bool,
        "type": str,
        "uuid": str,
        "voided_at": datetime,
    }


class InvoiceMini(Resource):
    """
    Attributes
    ----------
    number : str
        Invoice number
    state : str
        Invoice state
    """

    schema = {"number": str, "state": str}


class TransactionPaymentGateway(Resource):
    """
    Attributes
    ----------
    id : str
    name : str
    type : str
    """

    schema = {"id": str, "name": str, "type": str}


class AccountNote(Resource):
    """
    Attributes
    ----------
    account_id : str
    created_at : datetime
    id : str
    message : str
    user : User
    """

    schema = {
        "account_id": str,
        "created_at": datetime,
        "id": str,
        "message": str,
        "user": "User",
    }


class User(Resource):
    """
    Attributes
    ----------
    created_at : datetime
    deleted_at : datetime
    email : str
    first_name : str
    id : str
    last_name : str
    time_zone : str
    """

    schema = {
        "created_at": datetime,
        "deleted_at": datetime,
        "email": str,
        "first_name": str,
        "id": str,
        "last_name": str,
        "time_zone": str,
    }


class Subscription(Resource):
    """
    Attributes
    ----------
    account : AccountMini
    activated_at : datetime
        Activated at
    add_ons : :obj:`list` of :obj:`SubscriptionAddOn`
        Add-ons
    add_ons_total : float
        Total price of add-ons
    bank_account_authorized_at : datetime
        Recurring subscriptions paid with ACH will have this attribute set. This timestamp is used for alerting customers to reauthorize in 3 years in accordance with NACHA rules. If a subscription becomes inactive or the billing info is no longer a bank account, this timestamp is cleared.
    canceled_at : datetime
        Canceled at
    collection_method : str
        Collection method
    coupon_redemptions : :obj:`list` of :obj:`CouponRedemptionMini`
        Coupon redemptions
    created_at : datetime
        Created at
    currency : str
        3-letter ISO 4217 currency code.
    current_period_ends_at : datetime
        Current billing period ends at
    current_period_started_at : datetime
        Current billing period started at
    customer_notes : str
        Customer notes
    expiration_reason : str
        Expiration reason
    expires_at : datetime
        Expires at
    id : str
        Subscription ID
    net_terms : int
        Integer representing the number of days after an invoice's creation that the invoice will become past due. If an invoice's net terms are set to '0', it is due 'On Receipt' and will become past due 24 hours after it’s created. If an invoice is due net 30, it will become past due at 31 days exactly.
    pending_change : SubscriptionChange
    plan : PlanMini
    po_number : str
        For manual invoicing, this identifies the PO number associated with the subscription.
    quantity : int
        Subscription quantity
    remaining_billing_cycles : int
        Remaining billing cycles
    shipping_address : ShippingAddress
    state : str
        State
    subtotal : float
        Estimated total, before tax.
    terms_and_conditions : str
        Terms and conditions
    trial_ends_at : datetime
        Trial period ends at
    trial_started_at : datetime
        Trial period started at
    unit_amount : float
        Subscription unit price
    updated_at : datetime
        Last updated at
    uuid : str
        The UUID is useful for matching data with the CSV exports and building URLs into Recurly's UI.
    """

    schema = {
        "account": "AccountMini",
        "activated_at": datetime,
        "add_ons": ["SubscriptionAddOn"],
        "add_ons_total": float,
        "bank_account_authorized_at": datetime,
        "canceled_at": datetime,
        "collection_method": str,
        "coupon_redemptions": ["CouponRedemptionMini"],
        "created_at": datetime,
        "currency": str,
        "current_period_ends_at": datetime,
        "current_period_started_at": datetime,
        "customer_notes": str,
        "expiration_reason": str,
        "expires_at": datetime,
        "id": str,
        "net_terms": int,
        "pending_change": "SubscriptionChange",
        "plan": "PlanMini",
        "po_number": str,
        "quantity": int,
        "remaining_billing_cycles": int,
        "shipping_address": "ShippingAddress",
        "state": str,
        "subtotal": float,
        "terms_and_conditions": str,
        "trial_ends_at": datetime,
        "trial_started_at": datetime,
        "unit_amount": float,
        "updated_at": datetime,
        "uuid": str,
    }


class CouponRedemptionMini(Resource):
    """
    Attributes
    ----------
    coupon : CouponMini
    created_at : datetime
        Created at
    discounted : float
        The amount that was discounted upon the application of the coupon, formatted with the currency.
    id : str
        Coupon Redemption ID
    state : str
        Invoice state
    """

    schema = {
        "coupon": "CouponMini",
        "created_at": datetime,
        "discounted": float,
        "id": str,
        "state": str,
    }


class CouponMini(Resource):
    """
    Attributes
    ----------
    code : str
        The code the customer enters to redeem the coupon.
    coupon_type : str
        Whether the coupon is "single_code" or "bulk". Bulk coupons will require a `unique_code_template` and will generate unique codes through the `/generate` endpoint.
    discount : CouponDiscount
    expired_at : datetime
        The date and time the coupon was expired early or reached its `max_redemptions`.
    id : str
        Coupon ID
    name : str
        The internal name for the coupon.
    state : str
        Indicates if the coupon is redeemable, and if it is not, why.
    """

    schema = {
        "code": str,
        "coupon_type": str,
        "discount": "CouponDiscount",
        "expired_at": datetime,
        "id": str,
        "name": str,
        "state": str,
    }


class SubscriptionChange(Resource):
    """
    Attributes
    ----------
    activate_at : datetime
        Activated at
    activated : bool
        Returns `true` if the subscription change is activated.
    add_ons : :obj:`list` of :obj:`SubscriptionAddOn`
        These add-ons will be used when the subscription renews.
    created_at : datetime
        Created at
    deleted_at : datetime
        Deleted at
    id : str
        The ID of the Subscription Change.
    plan : PlanMini
    quantity : int
        Subscription quantity
    subscription_id : str
        The ID of the subscription that is going to be changed.
    unit_amount : float
        Unit amount
    updated_at : datetime
        Updated at
    """

    schema = {
        "activate_at": datetime,
        "activated": bool,
        "add_ons": ["SubscriptionAddOn"],
        "created_at": datetime,
        "deleted_at": datetime,
        "id": str,
        "plan": "PlanMini",
        "quantity": int,
        "subscription_id": str,
        "unit_amount": float,
        "updated_at": datetime,
    }


class SubscriptionAddOn(Resource):
    """
    Attributes
    ----------
    add_on : AddOnMini
    created_at : datetime
        Created at
    expired_at : datetime
        Expired at
    id : str
        Subscription Add-on ID
    quantity : int
        Add-on quantity
    subscription_id : str
        Subscription ID
    unit_amount : float
        This is priced in the subscription's currency.
    updated_at : datetime
        Updated at
    """

    schema = {
        "add_on": "AddOnMini",
        "created_at": datetime,
        "expired_at": datetime,
        "id": str,
        "quantity": int,
        "subscription_id": str,
        "unit_amount": float,
        "updated_at": datetime,
    }


class AddOnMini(Resource):
    """
    Attributes
    ----------
    accounting_code : str
        Accounting code for invoice line items for this add-on. If no value is provided, it defaults to add-on's code.
    code : str
        The unique identifier for the add-on within its plan.
    id : str
        Add-on ID
    name : str
        Describes your add-on and will appear in subscribers' invoices.
    """

    schema = {"accounting_code": str, "code": str, "id": str, "name": str}


class UniqueCouponCode(Resource):
    """
    Attributes
    ----------
    code : str
        The code the customer enters to redeem the coupon.
    created_at : datetime
        Created at
    expired_at : datetime
        The date and time the coupon was expired early or reached its `max_redemptions`.
    id : str
        Unique Coupon Code ID
    redeemed_at : datetime
        The date and time the unique coupon code was redeemed.
    state : str
        Indicates if the unique coupon code is redeemable or why not.
    updated_at : datetime
        Updated at
    """

    schema = {
        "code": str,
        "created_at": datetime,
        "expired_at": datetime,
        "id": str,
        "redeemed_at": datetime,
        "state": str,
        "updated_at": datetime,
    }


class Plan(Resource):
    """
    Attributes
    ----------
    accounting_code : str
        Accounting code for invoice line items for the plan. If no value is provided, it defaults to plan's code.
    code : str
        Unique code to identify the plan. This is used in Hosted Payment Page URLs and in the invoice exports.
    created_at : datetime
        Created at
    currencies : :obj:`list` of :obj:`dict`
        Pricing
    deleted_at : datetime
        Deleted at
    description : str
        Optional description, not displayed.
    hosted_pages : PlanHostedPages
        Hosted pages settings
    id : str
        Plan ID
    interval_length : int
        Length of the plan's billing interval in `interval_unit`.
    interval_unit : str
        Unit for the plan's billing interval.
    name : str
        This name describes your plan and will appear on the Hosted Payment Page and the subscriber's invoice.
    setup_fee_accounting_code : str
        Accounting code for invoice line items for the plan's setup fee. If no value is provided, it defaults to plan's accounting code.
    state : str
        Plans can be either active or inactive.
    tax_code : str
        Used by Avalara, Vertex, and Recurly’s EU VAT tax feature. The tax code values are specific to each tax system. If you are using Recurly’s EU VAT feature `P0000000` is `physical`, `D0000000` is `digital`, and an empty string is `unknown`.
    tax_exempt : bool
        `true` exempts tax on the plan, `false` applies tax on the plan.
    total_billing_cycles : int
        Automatically terminate subscriptions after a defined number of billing cycles. Number of billing cycles before the plan automatically stops renewing, defaults to `null` for continuous, automatic renewal.
    trial_length : int
        Length of plan's trial period in `trial_units`. `0` means `no trial`.
    trial_unit : str
        Units for the plan's trial period.
    updated_at : datetime
        Last updated at
    """

    schema = {
        "accounting_code": str,
        "code": str,
        "created_at": datetime,
        "currencies": list,
        "deleted_at": datetime,
        "description": str,
        "hosted_pages": "PlanHostedPages",
        "id": str,
        "interval_length": int,
        "interval_unit": str,
        "name": str,
        "setup_fee_accounting_code": str,
        "state": str,
        "tax_code": str,
        "tax_exempt": bool,
        "total_billing_cycles": int,
        "trial_length": int,
        "trial_unit": str,
        "updated_at": datetime,
    }


class PlanHostedPages(Resource):
    """
    Attributes
    ----------
    bypass_confirmation : bool
        If `true`, the customer will be sent directly to your `success_url` after a successful signup, bypassing Recurly's hosted confirmation page.
    cancel_url : str
        URL to redirect to on canceled signup on the hosted payment pages.
    display_quantity : bool
        Determines if the quantity field is displayed on the hosted pages for the plan.
    success_url : str
        URL to redirect to after signup on the hosted payment pages.
    """

    schema = {
        "bypass_confirmation": bool,
        "cancel_url": str,
        "display_quantity": bool,
        "success_url": str,
    }


class AddOn(Resource):
    """
    Attributes
    ----------
    accounting_code : str
        Accounting code for invoice line items for this add-on. If no value is provided, it defaults to add-on's code.
    code : str
        The unique identifier for the add-on within its plan.
    created_at : datetime
        Created at
    currencies : :obj:`list` of :obj:`AddOnPricing`
        Add-on pricing
    default_quantity : int
        Default quantity for the hosted pages.
    deleted_at : datetime
        Deleted at
    display_quantity : bool
        Determines if the quantity field is displayed on the hosted pages for the add-on.
    id : str
        Add-on ID
    name : str
        Describes your add-on and will appear in subscribers' invoices.
    plan_id : str
        Plan ID
    state : str
        Add-ons can be either active or inactive.
    tax_code : str
        Used by Avalara, Vertex, and Recurly’s EU VAT tax feature. The tax code values are specific to each tax system. If you are using Recurly’s EU VAT feature `P0000000` is `physical`, `D0000000` is `digital`, and an empty string is `unknown`.
    updated_at : datetime
        Last updated at
    """

    schema = {
        "accounting_code": str,
        "code": str,
        "created_at": datetime,
        "currencies": ["AddOnPricing"],
        "default_quantity": int,
        "deleted_at": datetime,
        "display_quantity": bool,
        "id": str,
        "name": str,
        "plan_id": str,
        "state": str,
        "tax_code": str,
        "updated_at": datetime,
    }


class AddOnPricing(Resource):
    """
    Attributes
    ----------
    currency : str
        3-letter ISO 4217 currency code.
    unit_amount : float
        Unit price
    """

    schema = {"currency": str, "unit_amount": float}