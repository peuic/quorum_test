from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Bill, Legislator, Vote, VoteResult

def home(request):
    return render(request, 'core/home.html')

def legislators(request):
    legislators = Legislator.objects.all()

    legislator_data = []
    for legislator in legislators:
        total_votes = VoteResult.objects.filter(legislator_id=legislator.id).count()
        votes_in_favor = VoteResult.objects.filter(legislator_id=legislator.id, vote_type=1).count()
        votes_against = VoteResult.objects.filter(legislator_id=legislator.id, vote_type=2).count()

        legislator_data.append({
            'id': legislator.id,
            'name': legislator.name,
            'total_votes': total_votes,
            'votes_in_favor': votes_in_favor,
            'votes_against': votes_against,
        })

    return render(request, 'core/legislators.html', {'legislator_data': legislator_data})

def bills(request):
    votes_in_favor = 0
    votes_against = 0
    bills = Bill.objects.all()

    bill_data = []
    for bill in bills:
        vote = Vote.objects.filter(bill_id=bill.id).first()

        if vote:
            votes_in_favor = VoteResult.objects.filter(vote_id=vote.id, vote_type=1).count()
            votes_against = VoteResult.objects.filter(vote_id=vote.id, vote_type=2).count()


        sponsor = Legislator.objects.filter(id=bill.sponsor_id).first()

        bill_data.append({
            'id': bill.id,
            'title': bill.title,
            'votes_in_favor': votes_in_favor,
            'votes_against': votes_against,
            'sponsor': sponsor.name if sponsor else "Unknown",
        })

    return render(request, 'core/bills.html', {'bill_data': bill_data})

def search(request):
    query = request.GET.get('q', '')
    legislators = Legislator.objects.filter(name__icontains=query) if query else []
    bills = Bill.objects.filter(title__icontains=query) if query else []

    return render(request, 'core/search_results.html', {
        'query': query,
        'legislators': legislators,
        'bills': bills,
    })

def legislator_detail(request, legislator_id):
    legislator = get_object_or_404(Legislator, id=legislator_id)
    votes = VoteResult.objects.filter(legislator_id=legislator.id)
    vote_data = []

    for vote in votes:
        bill = Bill.objects.filter(id=Vote.objects.filter(id=vote.vote_id).first().bill_id).first()
        vote_data.append({
            'bill_title': bill.title if bill else "Unknown",
            'bill_id': bill.id if bill else None,
            'vote_type': "Supporting" if vote.vote_type == 1 else "Opposing",
        })

    return render(request, 'core/legislator_detail.html', {
        'legislator': legislator,
        'vote_data': vote_data,
    })

def bill_detail(request, bill_id):
    votes_in_favor = 0
    votes_against = 0
    legislator_vote_data = []

    bill = get_object_or_404(Bill, id=bill_id)
    vote = Vote.objects.filter(bill_id=bill.id).first()

    if vote:
        legislator_votes = VoteResult.objects.filter(vote_id=vote.id)
        legislator_vote_data = [
            {
                'legislator_name': Legislator.objects.get(id=lv.legislator_id).name,
                'legislator_id': lv.legislator_id,
                'vote_type': "Supporting" if lv.vote_type == 1 else "Opposing",
            }
            for lv in legislator_votes
        ]

        votes_in_favor = legislator_votes.filter(vote_type=1).count()
        votes_against = legislator_votes.filter(vote_type=2).count()

    sponsor = Legislator.objects.filter(id=bill.sponsor_id).first()

    return render(request, 'core/bill_detail.html', {
        'bill': bill,
        'votes_in_favor': votes_in_favor,
        'votes_against': votes_against,
        'sponsor': sponsor.name if sponsor and sponsor.name else "Unknown",
        'sponsor_id': sponsor.id if sponsor else None,
        'legislator_vote_data': legislator_vote_data,
    })