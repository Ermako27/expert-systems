def contains(arr1, arr2):
    for elem in arr1:
        if elem not in arr2:
            return False
    
    return True

def removeClosedRules(closedRules, openedRules):
    newOpenedRules = []
    for openedRule in openedRules:
        isRuleToAdd = True
        for closedRule in closedRules:
            if closedRule.name == openedRule.name:
                isRuleToAdd = False
        
        if isRuleToAdd:
            newOpenedRules.append(openedRule)
    
    return newOpenedRules

def isReached(target, workingMemory):
    for node in workingMemory:
        if node == target:
            return True
    return False

def findClosedRules(workingMemory, openedRules):
    rulesQueue = []
    for rule in openedRules:
        antecedents = rule.antecedents
        isContains = contains(antecedents, workingMemory);
        if isContains:
            rulesQueue.append(rule)
    return rulesQueue;

def dataToTargetBFS(rules, initialWorkingMemory, target):
    openedRules = rules
    workingMemory = initialWorkingMemory

    # получаем закрытые правила
    rulesQueue = findClosedRules(workingMemory, openedRules)

    # проверяем не достигнута ли цель
    reached = isReached(target, workingMemory)
    # пока цель не достигнута и еще есть закрытые правила то продолжаем искать цель
    while not reached and len(rulesQueue) > 0:
        for rule in rulesQueue:
            workingMemory.extend(rule.consequent) # добавляем консеквенты закрытых правил в рабочую память

        openedRules = removeClosedRules(rulesQueue, openedRules) # удаляем из открытых правил, закрытые правила
        rulesQueue = findClosedRules(workingMemory, openedRules) # находим в рабочей памяти новые закрытые правила
        reached = isReached(target, workingMemory) # проверяем есть ли в рабочей памяти наша цель

    return reached, workingMemory



